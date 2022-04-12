import json
import visualize_plotly as vis
import visualize as vis2
import population as gen
import fitnesscalc as ft
import recombination as re
import mutation as mt
import nsga2 as ns
import survivor_selection as ss
import draw_pareto as pareto
from population import generate_pop
from tabulate import tabulate
from copy import deepcopy

from datetime import datetime

NUM_OF_ITERATIONS = 1
NUM_OF_INDIVIDUALS = 36
NUM_OF_GENERATIONS = 500
PC = int(0.8 * NUM_OF_INDIVIDUALS)
PM1 = 0.1
PM2 = 0.01
K = 2
ROTATIONS = 1

##MAIN##
if __name__ == "__main__":
    ## 1. LOADING TRUCK AND BOXS
    with open('data.json', 'r') as outfile:
        data = json.load(outfile)
    problem_indices = list(data.keys())

    for p_ind in problem_indices:
        start_time = datetime.now()
        print("################")
        print("Running Problem Set {}".format(p_ind))
        print(tabulate([['Generations', NUM_OF_GENERATIONS], ['Individuals', NUM_OF_INDIVIDUALS],
                        ['Rotations', ROTATIONS], ['Crossover Prob.', PC],
                        ['Mutation Prob1', PM1], ['Mutation Prob2', PM2], 
                        ['Tournament Size', K]], headers=['Parameter', 'Value'],
                        tablefmt="rst"))
        print("################")

        # Extracting inputs
        truck_dimension = data[p_ind]['truck dimension']
        packages = data[p_ind]['solution']
        boxes = data[p_ind]['boxes']
        total_value = data[p_ind]['total value']
        box_count = data[p_ind]['number']
        box_params = {}
        for index in range(len(boxes)):
            box_params[index] = boxes[index]

        # Storing the average values over every single iteration
        average_vol = []
        average_num = []
        average_value = []
        remain_vol = []

        for i in range(NUM_OF_ITERATIONS):
            # Generate the initial population
            # print(gen,box_params,NUM_OF_INDIVIDUALS,ROTATIONS)
            population = generate_pop(box_params, NUM_OF_INDIVIDUALS, ROTATIONS)
           #print(population)

            gen = 0
            average_fitness = []

            while gen < NUM_OF_GENERATIONS:
                ## evaluate
                population, fitness = ft.evaluate(population, truck_dimension, box_params, total_value)
                population = ns.rank(population, fitness)
                offsprings = re.crossover(deepcopy(population), PC, k=K)
                offsprings = mt.mutate(offsprings, PM1, PM2, ROTATIONS)
                population = ss.select(population, offsprings, truck_dimension, box_params, total_value,
                                       NUM_OF_INDIVIDUALS)
                average_fitness.append(ft.calc_average_fitness(population))
                gen += 1
            
            end_time = datetime.now()
            results = []
            #print(average_fitness)
            # Storing the final Rank 1 solutions
            for key, value in population.items():
                if value['Rank'] == 1:
                    results.append(value['result'])

            #print(results)
            # Plot using plotly
            color_index = vis.draw_solution(pieces=packages)
            vis.draw(results, color_index)

            # Plot using matplotlib
            color_index = vis2.draw(pieces=packages, title="Giai phap Goc")
            for each in results:
                vis2.draw(each, color_index, title="Giải pháp tối ưu {}".format(i))
            pareto.draw_pareto(population)
            average_vol.append(average_fitness[-1][0])
            average_num.append(average_fitness[-1][1])
            average_value.append(average_fitness[-1][2])
            remain_vol.append(average_fitness[-1][3])
            pareto.plot_stats(average_fitness,
                       title="Giá trị thích nghi trung bình - Lần chạy {} qua {} thế hệ".format(i + 1,NUM_OF_GENERATIONS))


        print("Result: ")
        print(remain_vol)
        print(tabulate(
            [['Problem Set', p_ind], ['Runs', NUM_OF_ITERATIONS], 
             ['Avg. Volume%', sum(average_vol) / len(average_vol)],
             ['Avg. Number%', sum(average_num) / len(average_num)],
             ['Avg. Value%', sum(average_value) / len(average_value)]],
            headers=['Parameter', 'Value'], 
            tablefmt="rst"))
        print("##############################")
        print("Running Time Problem Set {}".format(p_ind))
        print('Duration: {}'.format(end_time - start_time))
        print("##############################")