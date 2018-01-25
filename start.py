
import funcs as f
from funcs import AnimalFood


def txt_to_var(file):
    File = open(file, "r")
    _table = []
    while (1):
        _line = File.readline()
        if _line == "":
            return _table
        _table.append(_line)
    File.close()
    return _table


table = txt_to_var('output2.txt')

animal_foods = []
i = 1

for line in table:
    try:
        food = AnimalFood(line)
        print(i, ' - All ok: '+ food.name)
        animal_foods.append(food)
        i += 1
    except:
        print('failed to add: ' + line)
    if i == 10:
        f.save_obj(animal_foods, 'karma_10')
    if i == 100:
        f.save_obj(animal_foods, 'karma_100')
    if i == 200:
        f.save_obj(animal_foods, 'karma_200')

f.save_obj(animal_foods, 'karma_ALL')