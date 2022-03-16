import fitnesscalc as ft
import nsga2 as ns


def select(population, offsprings, truck, boxes, total_value, count):
    survive = {}
    offspring, fitness = ft.evaluate(offsprings, truck, boxes, total_value)
    offspring = ns.rank(offspring, fitness)
    pool = list(population.values()) + list(offspring.values())
    i = 1
    while len(survive) < count:
        group = [values for values in pool if values['Rank'] == i]

 
        if len(group) <= count - len(survive):
            j = 0
            for index in range(len(survive), len(survive)+len(group)):
                survive[index] = group[j]
                j += 1

        else:
            group = sorted(group, key=lambda x: x['CD'], reverse=True)
            j = 0
            for index in range(len(survive), count):
                survive[index] = group[j]
                j += 1
        i += 1

    return survive
