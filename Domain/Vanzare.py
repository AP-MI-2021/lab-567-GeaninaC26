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
    return {
        'id' : id_vanzare,
        'titlu': titlu,
        'gen': gen,
        'pret': pret,
        'reducere': reducere,
    }


def get_id(vanzare):
    """
    Getter pentru id-ul vanzarii.
    :param vanzare: vanzarea
    :return: id-ul vanzarii date ca parametru
    """
    return vanzare['id']


def get_titlu(vanzare):
    """
    Getter pentru numele vanzarii.
    :param vanzare: vanzarea
    :return: numele vanzarii date ca parametru
    """
    return vanzare['titlu']


def get_gen(vanzare):
    """
    Getter pentru genul vanzarii.
    :param vanzare: vanzarea
    :return: genul vanzarii date ca parametru
    """
    return vanzare['gen']


def get_pret(vanzare):
    """
    Getter pentru pretul vanzarii.
    :param vanzare: vanzarea
    :return: pretul vanzarii date ca parametru
    """
    return vanzare['pret']


def get_reducere(vanzare):
    """
    Getter pentru reducerea vanzarii.
    :param vanzare: vanzarea
    :return: tipul reducerii vanzarii date ca parametru
    """
    return vanzare['reducere']


def get_str(vanzare):
    return f'Vanzarea cu id {get_id(vanzare)}, titlu {get_titlu(vanzare)}, gen {get_gen(vanzare)}, pret {get_pret(vanzare)}, reducere {get_reducere(vanzare)}'

