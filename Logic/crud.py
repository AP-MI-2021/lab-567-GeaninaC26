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
    vanzare = creeaza_vanzare(id_vanzare, titlu, gen, pret, reducere)
    return lst_vanzari + [vanzare]


def read(lst_vanzari, id_vanzare: int = None):
    """
    Citeste vanzarea
    :param lst_vanzari: lista de vanzari
    :param id_vanzare: id-ul vanzarii pe care dorim sa o citim
    :return: vanzarea cu id-ul id_vanzare, sau None daca vanzarea nu exista
    """
    for vanzare in lst_vanzari:
        if int(get_id(vanzare)) == id_vanzare:
            return vanzare
    return None


def update(lst_vanzari, new_vanzare):
    """
    Actualizeaza o
    :param lst_vanzari: lista de vanzari
    :param new_vanzare: vanzarea cu care se va actualiza - id-ul trebuie sa fie unul existent
    :return: lista cu vanzarile actualizare
    """
    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != get_id(new_vanzare):
            new_vanzari.append(new_vanzare)
    return new_vanzari


def delete(lst_vanzari, id_vanzare: int):
    """
    Sterge din lista de vanzari, vanzarea cu id-ul id_vanzare
    :param lst_vanzari: lista de vanzari
    :param id_vanzare: id-ul vanzarii care se sterge
    :return: o lista fara vanzarea cu id-ul id_vanzare
    """
    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != id_vanzare:
            new_vanzari.append(vanzare)
    return new_vanzari