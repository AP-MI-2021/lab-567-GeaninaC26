from Domain.Vanzare import creeaza_vanzare, get_id


def create(lst_vanzari, id_vanzare, titlu, gen, pret, reducere):
    vanzare = creeaza_vanzare(id_vanzare, titlu, gen, pret, reducere)
    return lst_vanzari + [vanzare]


def read(lst_vanzari, id_vanzare: int=None):
    vanzare_cu_id = None
    for vanzare in lst_vanzari:
        if vanzare['id'] == id_vanzare:
            vanzare_cu_id = id_vanzare
        if vanzare_cu_id:
            return vanzare_cu_id
    return lst_vanzari


def update(lst_vanzari, new_vanzare):
    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != get_id(new_vanzare):
            new_vanzari.append(new_vanzare)
    return new_vanzari


def delete(lst_vanzari, id_vanzare: int):
    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != id_vanzare:
            new_vanzari.append(vanzare)
    return new_vanzari