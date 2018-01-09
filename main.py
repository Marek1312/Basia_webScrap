import urllib.request
from bs4 import BeautifulSoup

txt = "output2.txt"


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

class AnimalFood(object):
    def __init__(self, name,url, animal):
        self.name = name
        self.url = url
        self.animal = animal
    def __str__(self):
        return ' Karma: %s \n Przeznaczenie: %s \n url: %s' %(self.name, self.animal, self.url)


def scrap_food(_url):
    # url to soup object
    soup = BeautifulSoup(urllib.request.urlopen(_url), 'html.parser')
    def get_name(soup):
        try:
            name_box = soup.find('h1', attrs={'class': 'producttitle'})
            _name = name_box.text.strip()  # strip() is used to remove starting and trailing
        except:
            return
        return _name
    food = AnimalFood(name = get_name(soup), url = _url, animal = "cat")

    return food


table = txt_to_var(txt)

food0001 = scrap_food(table[55])
print(food0001)


