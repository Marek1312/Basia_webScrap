'''Wyświetlanie danej liczby obieków z najniższą wartością klucza'''
def f_filter(key, n):
    def getKey(custom):
        return custom.composition[key]
    new_items = []
    for item in testy:
        try:
            item.composition[key]
            new_items.append(item)
        except:
            pass
    new_items.sort(key=getKey)
    print(key + ': ')
    for j in range(n):
        print(new_items[j].name +' - ', new_items[j].composition[key] , '%')