from Domain.Vanzare import get_reducere, get_pret, set_new_price, get_titlu, set_new_genre, get_id_by_title, get_gen


def aplicare_discount(lst_vanzari, undo_list: list, redo_list: list):
    """
    Reduce pretul vanzarii in functie de reducere : 0 pentru none, 5% pentru reducere silver, 10% pentru reducere gold.
    :param lst_vanzari: lista de vanzari
    :return: lista cu preturile reduse
    """
    undo_list.append(lst_vanzari)
    redo_list.clear()
    for vanzare in lst_vanzari:
        if get_reducere(vanzare) == 'silver':
            price = get_pret(vanzare)
            new_price = price - 0.05*price
            set_new_price(vanzare, new_price)
        if get_reducere(vanzare) == 'gold':
            price = get_pret(vanzare)
            new_price = price - 0.1 * price
            set_new_price(vanzare, new_price)
    return lst_vanzari


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
    for vanzare in lst_vanzari:
        if get_titlu(vanzare) == titlu:
            set_new_genre(vanzare,gen_nou)
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
        redo_list.append(vanzari)
        return top_redo
    return None