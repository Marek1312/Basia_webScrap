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
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(urllib.request.urlopen(self.url), 'html.parser')
        self.get_name()


    def __str__(self):
        return ' Karma: %s \n url: %s' %(self.name, self.url)

    def get_name(self):
        try:
            name_box = self.soup.find('h1', attrs={'class': 'producttitle'})
            _name = name_box.text.strip()  # strip() is used to remove starting and trailing
            self.name = _name
        except:
            return
        return _name

    def get_price(self):
        prices = self.soup.findAll('div', attrs={'class': 'clearfix product__offer '})
        x = {}
        for price in prices:
            x.update({(price.find('div', attrs={'class': 'product__varianttitle'})).text[0:120].strip():
                          (price.find('span', attrs={'class': 'price__amount'})).text.strip()})
        return x


### main frame ###
table = txt_to_var(txt)

food1 = AnimalFood(table[55])





