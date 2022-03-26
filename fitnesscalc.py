from operator import itemgetter
from copy import deepcopy
import csv
filename = "remain.csv"

def evaluate(population, truck_dimension, boxes, total_value):
    
    container_vol = truck_dimension[0] * truck_dimension[1] * truck_dimension[2]
    ft = {}
    remain_box = []
    for key, individual in population.items():
        dblf = [[0, 0, 0] + truck_dimension]
        occupied_vol = 0
        number_boxes = 0
        value = 0
        result = []
        for box_number, r in zip(individual['order'], individual['rotate']):
            #print(box_number,r)
            dblf = sorted(dblf, key=itemgetter(3))
            #print(dblf)
            dblf = sorted(dblf, key=itemgetter(5))
            #print(dblf)
            dblf = sorted(dblf, key=itemgetter(4))
            #print(dblf)
            if r == 0:
                l, w, h = boxes[box_number][0:3]
            elif r == 1:
                w, l, h = boxes[box_number][0:3]
            elif r == 2:
                l, h, w = boxes[box_number][0:3]
            elif r == 3:
                h, l, w = boxes[box_number][0:3]
            elif r == 4:
                h, w, l = boxes[box_number][0:3]
            else:
                w, h, l = boxes[box_number][0:3]

            #print(pos)
            for pos in dblf:
                current = deepcopy(pos)
                space_vol = pos[3] * pos[4] * pos[5]
                box_vol = boxes[box_number][3]
                box_value = boxes[box_number][4]

                if space_vol >= box_vol and pos[3] >= l and pos[4] >= w and pos[5] >= h:
                    result.append(pos[0:3] + [l, w, h])
                    occupied_vol += box_vol
                    number_boxes += 1
                    value += box_value
                    top_space = [pos[0], pos[1], pos[2] + h, l, w, pos[5] - h]
                    beside_space = [pos[0], pos[1] + w, pos[2], l, pos[4] - w, pos[5]]
                    front_space = [pos[0] + l, pos[1], pos[2], pos[3] - l, pos[4], pos[5]]
                    #print(top_space,beside_space,front_space)
                    dblf.remove(current)
                    dblf.append(top_space)
                    dblf.append(beside_space)
                    dblf.append(front_space)
                    break
                #else:
                    #fields = ['The tich con lai', occupied_vol, 'Hop can xep',[l,w,h], 'The tich con lai',[pos[3],pos[4],pos[5]]]
                    #remain_box.append(fields)
                    
        #print(dblf[-1])

        #print(box_number)
        if r == 0:
            l, w, h = boxes[box_number][0:3]
        elif r == 1:
            w, l, h = boxes[box_number][0:3]
        elif r == 2:
            l, h, w = boxes[box_number][0:3]
        elif r == 3:
            h, l, w = boxes[box_number][0:3]
        elif r == 4:
            h, w, l = boxes[box_number][0:3]
        else:
            w, h, l = boxes[box_number][0:3]
        fields = ['The tich da xep: ', occupied_vol, 'Hop con lai: ',[l,w,h], 'The tich con lai: ',dblf[-1][3:6]]
        print(fields)
        #print(dblf[-1][3:6])
        #print(dblf)
                

                    #print(space_vol)
                    #print("Hop can xep: ",[l,w,h])
                    #print("The tich con lai: ",[pos[3],pos[4],pos[5]])
                    #break
        #print(dblf)
        
        #print(remain_box)
        avg_vol = 0
        #print(occupied_vol)
        remain_vol = container_vol - occupied_vol
        if (number_boxes == len(list(boxes.keys()))):
            avg_vol = remain_vol/container_vol * 100
        else:
            avg_vol = round((occupied_vol / container_vol * 100), 2)

            avg_vol = round((occupied_vol / container_vol * 100), 2)
        #remain_vol = container_vol - occupied_vol
        #print(remain_vol)
        fitness = [avg_vol, round((number_boxes / len(list(boxes.keys())) * 100), 2),
             round((value / total_value * 100), 2)]
        #round(remain_vol/container_vol * 100,2)
        ft[key] = fitness
        population[key]['fitness'] = deepcopy(fitness)
        population[key]['result'] = result
    return population, ft

def calc_average_fitness(individuals):
    fitness_sum = [0.0, 0.0, 0.0, 0.0]
    count = 0
    for key, value in individuals.items():
        if value['Rank'] == 1:
            count += 1
            fitness_sum[0] += value['fitness'][0]
            fitness_sum[1] += value['fitness'][1]
            fitness_sum[2] += value['fitness'][2]


    if (count == 0):
        average = [0, 0, 0]
    else:
        average = [number / count for number in fitness_sum]
    return average