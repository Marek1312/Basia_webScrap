import _pickle as pickle
import urllib.request
from bs4 import BeautifulSoup


class AnimalFood(object):
    def __init__(self, url):
        self.url = url
        self.name = get_name(url)
        self.price = get_price(url)
        self.composition = get_composition(url)

    def __str__(self):
        return ' Karma: %s \n url: %s' %(self.name, self.url)


def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f)


def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


def low_fosfor(Foods):
    x = []
    for key, value in Foods.items():
        try:
            #x += [(key, float(value.composition['Fosfor'].strip(' %')))]
            print(key + 'ma :' + float(value.composition['Fosfor'].strip('%') + '% Fosforu'))
        except :
            print(key + ' nie udostepnia ilości fosforu')
    return x


def make_soup(url):
    return BeautifulSoup(urllib.request.urlopen(url), 'html.parser')


def get_name(url):
    soup = make_soup(url)
    return soup.find('h1', attrs={'class': 'producttitle'}).text.strip()


def get_composition(url):
    soup = make_soup(url)
    return {x.find_all('td')[0].text : float(x.find_all('td')[1].text.strip('% kcal g/kg mg/kg mg IE/kg')) for x in
                   soup.find_all('table')[1].find_all('tr')}


def get_price(url):
    soup = make_soup(url)
    prices = soup.findAll('div', attrs={'class': 'clearfix product__offer '})
    x = {}
    for price in prices:
        x.update({(price.find('div', attrs={'class': 'product__varianttitle'})).text[0:120].strip():
                      (price.find('span', attrs={'class': 'price__amount'})).text.strip()})
    return x

