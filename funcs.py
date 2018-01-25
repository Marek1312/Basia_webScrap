import _pickle as pickle
import urllib.request
from bs4 import BeautifulSoup


class AnimalFood(object):
    tab_suffix = {'Białko surowe': '%', 'Tłuszcz surowy': '%', 'Włókno surowe': '%', 'Popiół surowy': '%',
                       'Wapń': '%', 'Fosfor': '%', 'Wilgotność': '%'}

    def __init__(self, url):
        self.url = url
        soup = self.make_soup(url)
        self.name = get_name(soup)
        self.price = get_price(soup)
        self.composition = get_composition(soup)
        self.description, self.addons = get_description(soup)

    def make_soup(self, url):
        return BeautifulSoup(urllib.request.urlopen(url), 'html.parser')

    def __str__(self):
        return ' Karma: %s \n url: %s' %(self.name, self.url)


def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f)


def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


def get_name(soup):
    return soup.title.text


def get_composition(soup):
    return {x.find_all('td')[0].text : float(x.find_all('td')[1].text.strip('% kcal g/kg mg/kg mg IE/kg')) for x in
                   soup.find_all('table')[1].find_all('tr')}


def get_price(soup):
    prices = soup.findAll('div', attrs={'class': 'clearfix product__offer '})
    x = {}
    for price in prices:
        x.update({(price.find('div', attrs={'class': 'product__varianttitle'})).text[0:120].strip():
                      (price.find('span', attrs={'class': 'price__amount'})).text.strip()})
    return x


def get_description(soup):
    desc = (soup.find('article', attrs={'col-md-10 col-md-push-1'}))


    return [desc, addons]





