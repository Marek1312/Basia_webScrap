
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

for line in table[0:50]:
    food = AnimalFood(line)
    animal_foods.append(food)

f.save_obj(animal_foods, 'karma')
