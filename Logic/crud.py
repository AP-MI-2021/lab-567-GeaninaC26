from Domain.Vanzare import creeaza_vanzare, get_id


def create(lst_vanzari, id_vanzare, titlu, gen, pret, reducere, undo_list: list, redo_list: list):
    """
    Adauga o vanzare in lista.
    :param lst_vanzari: lista de vanzari
    :param id_vanzare: id-ul vanzarii
    :param titlu: titlul cartii
    :param gen: genul cartii
    :param pret: pretul cartii
    :param reducere: reducerea clientului
    :param undo_list:
    :param redo_list:
    :return:
    """
    if read(lst_vanzari, id_vanzare ) is not None:
        raise ValueError(f'Exista deja o vanzare cu id-ul {id_vanzare}')

    vanzare = creeaza_vanzare(id_vanzare, titlu, gen, pret, reducere)

    undo_list.append(lst_vanzari)
    redo_list.clear()

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


def update(lst_vanzari, new_vanzare, undo_list, redo_list):
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
    undo_list.append(lst_vanzari)
    redo_list.clear()
    return new_vanzari



def delete(lst_vanzari, id_vanzare: int, undo_list, redo_list):
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
    undo_list.append(lst_vanzari)
    redo_list.clear()
    return new_vanzari


def generare():
    vanzari = []
    vanzari = create(vanzari, '1', 'Harry Potter', 'Fictiune', 45, 'silver', [], [])
    vanzari = create(vanzari, '2', 'La rascruce de vanturi', 'Roman', 35, 'none', [], [])
    vanzari = create(vanzari, '3', 'Moara cu noroc', 'Fictiune', 20, 'gold', [], [])
    vanzari = create(vanzari, '4', 'Ion', 'Realism', 30, 'none', [], [])
    vanzari = create(vanzari, '5', 'Descult', 'Roman', 50, 'silver', [], [])

    return vanzari