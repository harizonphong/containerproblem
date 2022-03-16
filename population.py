import random
from copy import deepcopy


def generate_pop(box_params, count, rotation=5):
    #[l, w, h, vol, value]

    population = {}
    if count > 5:
        x = 5
    else:
        x = count
    for i in range(0, x):
        sorted_box = dict(sorted(box_params.items(), key=lambda x: x[1][i]))
        population[i] = {"order": list(sorted_box.keys()),
                         "rotate": [random.randint(0, rotation - 1) for r in range(len(box_params))]}

    keys = list(box_params.keys())
    for i in range(5, count):
        random.shuffle(keys)
        population[i] = {"order": deepcopy(keys),
                         "rotate": [random.randint(0, rotation - 1) for r in range(len(box_params))]}
    return population
