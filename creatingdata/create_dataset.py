import json
import random
import boxes as box

MIN_VALUE = 50
MAX_VALUE = 500


truck_dim = [[587, 228, 259]]

NUM_BOXES = [[7]]

dataset = {}
i = 0
print(truck_dim)
print(NUM_BOXES)
for cont, counts in zip(truck_dim, NUM_BOXES):
    print(cont,counts)
    for number in counts:
        packages = box.generateboxes([[0, 0, 0] + cont], number)
        boxes = []
        total_value = 0
        for each in packages:
            l, w, h = each[3:]
            vol = l * w * h
            value = random.randint(MIN_VALUE, MAX_VALUE)
            total_value += value
            boxes.append([l, w, h, vol, value])
        dataset[i] = {'truck dimension': cont, 'number': number, 'boxes': boxes, 'solution': packages,
                      'total value': total_value}
        i += 1

with open('datasetnew.json', 'w') as outfile:
    json.dump(dataset, outfile)
