def creeaza_vanzare(id_vanzare, titlu, gen, pret, reducere):
    """
    Creeaza vanzarea
    :param id_vanzare: id-ul vanzarii, trebuie sa fie unic
    :param titlu: titlul cartii, nenul
    :param gen: genul cartii
    :param pret: pretul cartii
    :param reducere: reducerea vanzarii (none, silver, gold
    :return:
    """
    return  [
         id_vanzare,
         titlu,
         gen,
         pret,
         reducere,
    ]



def get_id(vanzare):
    """
    Getter pentru id-ul vanzarii.
    :param vanzare: vanzarea
    :return: id-ul vanzarii date ca parametru
    """
    return vanzare[0]


def get_titlu(vanzare):
    """
    Getter pentru numele vanzarii.
    :param vanzare: vanzarea
    :return: numele vanzarii date ca parametru
    """
    return vanzare[1]


def get_gen(vanzare):
    """
    Getter pentru genul vanzarii.
    :param vanzare: vanzarea
    :return: genul vanzarii date ca parametru
    """
    return vanzare[2]


def get_pret(vanzare):
    """
    Getter pentru pretul vanzarii.
    :param vanzare: vanzarea
    :return: pretul vanzarii date ca parametru
    """
    return vanzare[3]


def get_reducere(vanzare):
    """
    Getter pentru reducerea vanzarii.
    :param vanzare: vanzarea
    :return: tipul reducerii vanzarii date ca parametru
    """
    return vanzare[4]


def get_str(vanzare):
    return f'Vanzarea cu id {get_id(vanzare)}, titlu {get_titlu(vanzare)}, gen {get_gen(vanzare)}, pret {get_pret(vanzare)}, reducere {get_reducere(vanzare)}'


def set_new_price(vanzare, new_price):
    """
    Inlocuieste pretul vanzarii cu un nou pret.
    :param vanzare: vanzarea
    :param new_price: pretul cu care se inlocuieste pretul initial.
    :return:
    """
    vanzare[3] = new_price


def set_new_genre(vanzare, new_genre):
    """
    Inlocuieste genul vanzarii cu un nou pret.
    :param vanzare: vanzarea
    :param gen_nou: genul cu care se inlocuieste genul initial.
    :return:
    """
    vanzare[2] = new_genre


def get_id_by_title(vanzare, titlu):
    if vanzare[1] == titlu :
        return vanzare[0]