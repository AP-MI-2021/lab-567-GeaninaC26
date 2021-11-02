from Domain.Vanzare import creeaza_vanzare, get_id


def create(lst_vanzari, id_vanzare, titlu, gen, pret, reducere):
    """
    Adauga o vanzare in lista.
    :param lst_vanzari: lista de vanzari
    :param id_vanzare: id-ul vanzarii
    :param titlu: titlul cartii
    :param gen: genul cartii
    :param pret: pretul cartii
    :param reducere: reducerea clientului
    :return:
    """
    if read(lst_vanzari, id_vanzare ) is not None:
        raise ValueError(f'Exista deja o vanzare cu id-ul {id_vanzare}')
    vanzare = creeaza_vanzare(id_vanzare, titlu, gen, pret, reducere)
    return lst_vanzari + [vanzare]


def read(lst_vanzari, id_vanzare: int = None):
    """
    Citeste vanzarea
    :param lst_vanzari: lista de vanzari
    :param id_vanzare: id-ul vanzarii pe care dorim sa o citim
    :return: -vanzarea cu id-ul id_vanzare
             -None daca nu exista o vanzare cu id_prajitura
             -lista de vanzari, daca id_vanzare = None
    """

    if id_vanzare is None:
        return lst_vanzari

    for vanzare in lst_vanzari:
        if get_id(vanzare) == id_vanzare:
            return vanzare
    return None


def update(lst_vanzari, new_vanzare):
    '''
    Modifica vanzarea cu id-ul dat
    :param id:
    :param titlu_carte:
    :param gen_carte:
    :param pret:
    :param tip_reducere:
    :return:
    '''
    if read(lst_vanzari, get_id(new_vanzare) ) is None:
        raise ValueError(f'Nu exista o vanzare cu id-ul {get_id(new_vanzare)}')
    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) == get_id(new_vanzare):
            new_vanzari.append(new_vanzare)
        else:
            new_vanzari.append(vanzare)
    return new_vanzari



def delete(lst_vanzari, id_vanzare: int):
    """
    Sterge din lista de vanzari, vanzarea cu id-ul id_vanzare
    :param lst_vanzari: lista de vanzari
    :param id_vanzare: id-ul vanzarii care se sterge
    :return: o lista fara vanzarea cu id-ul id_vanzare
    """
    if read(lst_vanzari, id_vanzare ) is None:
        raise ValueError(f'Nu exista o vanzare cu id-ul {id_vanzare}')
    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != id_vanzare:
            new_vanzari.append(vanzare)
    return new_vanzari