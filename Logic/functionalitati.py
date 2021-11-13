from Domain.Vanzare import get_reducere, get_pret, set_new_price, get_titlu, get_id, get_id_by_title, get_gen, creeaza_vanzare
from Logic.crud import update

def aplicare_discount(lst_vanzari, undo_list: list, redo_list: list):
    """
    Reduce pretul vanzarii in functie de reducere : 0 pentru none, 5% pentru reducere silver, 10% pentru reducere gold.
    :param lst_vanzari: lista de vanzari
    :return: lista cu preturile reduse
    """
    new_lst = []
    for vanzare in lst_vanzari:
        if get_reducere(vanzare) == 'silver':
            id = get_id(vanzare)
            titlu = get_titlu(vanzare)
            gen = get_gen(vanzare)
            price = get_pret(vanzare)- get_pret(vanzare) * 0.05
            reducere = get_reducere(vanzare)
            vanzare_noua = creeaza_vanzare(id, titlu,gen,price, reducere)
            new_lst.append(vanzare_noua)
        elif get_reducere(vanzare) == 'gold':
            id = get_id(vanzare)
            titlu = get_titlu(vanzare)
            gen = get_gen(vanzare)
            price = get_pret(vanzare) - get_pret(vanzare) * 0.1
            reducere = get_reducere(vanzare)
            vanzare_noua = creeaza_vanzare(id, titlu, gen, price, reducere)
            new_lst.append(vanzare_noua)
        else:
            new_lst.append(vanzare)
    undo_list.append(lst_vanzari)
    redo_list.clear()
    return new_lst


def modificare_gen(lst_vanzari, titlu, gen_nou, undo_list: list, redo_list: list):
    """
    Modifica genul unei vanzari cu titlu dat.
    :param lst_vanzari: lista de vanzari.
    :param titlu: titlul vanzarii.
    :param gen_nou: noul gen al vanzarii cu titlu dat
    :return: lista de vanzari, in care vanzarile cu titlul 'titlu' au genul 'gen_nou'
    """
    undo_list.append(lst_vanzari)
    redo_list.clear()
    check = 0
    for vanzare in lst_vanzari:
        title = get_titlu(vanzare)
        if title == titlu:
            check = 1
    if check == 0:
        print(f'Nu exista o vanzare cu titlul {titlu}')
    else:
        for vanzare in lst_vanzari:
            if get_titlu(vanzare) == titlu:
                id = get_id(vanzare)
                pret = get_pret(vanzare)
                reducere = get_reducere(vanzare)
                lst_vanzari = update(lst_vanzari, creeaza_vanzare(id, titlu, gen_nou, pret, reducere), undo_list, redo_list)
    return lst_vanzari


def determinare_pret_minim(lst_vanzari):
    """
    Determina pretul minim pentru fiecare gen.
    :param lst_vanzari: lista de vanzari
    :return:
    """
    result = {}
    for vanzare in lst_vanzari:
        gen = get_gen(vanzare)
        pret = get_pret(vanzare)
        if gen in result:
            if pret < result[gen]:
                result[gen] = pret
        else:
            result[gen] = pret
    return result


def sortare_in_functie_de_pret(lst_vanzari, undo_list: list, redo_list: list):
    '''
    Sorteaza lista crescator in functie de pret.
    :param lista: lista de vanzari
    :return: lista de vanzari sortata
    '''
    undo_list.append(lst_vanzari)
    redo_list.clear()
    return sorted(lst_vanzari, key=lambda x: get_pret(x))


def nr_titluri_gen(gen, lst_vanzari):
    lista_titluri = []
    for vanzare in lst_vanzari:
        if get_gen(vanzare) == gen:
            lista_titluri.append(get_titlu(vanzare))

    set_lista_titluri = set(lista_titluri)
    lista_fara_duplicate = list(set_lista_titluri)

    return len(lista_fara_duplicate)


def nr_titluri_distincte_pe_gen(lst_vanzari):
    '''
    Determina pentru fiecare gen, numarul de titluri distincte
    :param lista: lista de vanzari
    :return: dictionar care are ca si cheie numele genului,
    iar ca valoare numarul de titluri distincte pentru acel gen
    '''
    rezultat = {}
    for vanzare in lst_vanzari:
        gen = get_gen(vanzare)
        if gen not in rezultat:
            rezultat[gen] = nr_titluri_gen(gen, lst_vanzari)

    return rezultat


def do_undo(undo_list: list, redo_list: list, vanzari):
    '''

    :param undo_list:lista cu actiunile facute
    :param redo_list:lista cu actiunile anulate
    '''
    if undo_list:
        top_undo = undo_list.pop()
        redo_list.append(vanzari)
        return top_undo
    return None


def do_redo(undo_list:list, redo_list: list, vanzari):
    '''
    :params undo_list: lista cu actiunile facute
    :params redo_list: lista cu actiunile anulate
    '''
    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(vanzari)
        return top_redo
    return None