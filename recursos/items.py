def get_initial_items(soup): #
    """ Funcion que muestra en pantalla los objetos iniciales recomendados. """
    # div class  _dtoou _iqcim1 _dcqhsp
    initials_soup = soup.find_all("div",class_="_dtoou _iqcim1 _dcqhsp")
    initials_soup_listed = [elem for elem in initials_soup[0].find_all('img')]
    initials_list = [] # para mayor entendimiento lo dejaré asi
    for elem in initials_soup_listed:
        initials_list.append(elem.get('alt')) # Hago lista de los alt de las imagenes, lo cual es basicamente el nombre del objeto
    print (" - ".join(initials_list))

def get_items(soup):
    items_soup = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['_9jhm56'])
    # aca listamos las imagenes del soup
    item_soup_listed = [elem for elem in items_soup[0].find_all('img')]
    item_list = [] # para mayor entendimiento lo dejaré asi
    for elem in item_soup_listed:
        item_list.append(elem.get('alt')) # Hago lista de los alt de las imagenes, lo cual es basicamente el nombre del objeto
    print(" - ".join(item_list[:-2]))

