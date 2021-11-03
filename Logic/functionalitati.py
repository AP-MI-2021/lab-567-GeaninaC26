from Domain.Vanzare import get_reducere, get_pret, set_new_price, get_titlu, set_new_genre, get_id_by_title, get_gen


def aplicare_discount(lst_vanzari):
    """
    Reduce pretul vanzarii in functie de reducere : 0 pentru none, 5% pentru reducere silver, 10% pentru reducere gold.
    :param lst_vanzari: lista de vanzari
    :return: lista cu preturile reduse
    """
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


def modificare_gen(lst_vanzari, titlu, gen_nou):
    """
    Modifica genul unei vanzari cu titlu dat.
    :param lst_vanzari: lista de vanzari.
    :param titlu: titlul vanzarii.
    :param gen_nou: noul gen al vanzarii cu titlu dat
    :return: lista de vanzari, in care vanzarile cu titlul 'titlu' au genul 'gen_nou'
    """
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