def creeaza_vanzare(id_vanzare, titlu, gen, pret, reducere):
    return {
        'id' : id_vanzare,
        'titlu': titlu,
        'gen': gen,
        'pret': pret,
        'reducere': reducere,
    }


def get_id(vanzare):
    return vanzare['id']


def get_titlu(vanzare):
    return vanzare['titlu']


def get_gen(vanzare):
    return vanzare['gen']


def get_pret(vanzare):
    return vanzare['pret']


def get_reducere(vanzare):
    return vanzare['reducere']


def get_str(vanzare):
    return f'Vanzarea cu id {get_id(vanzare)}, titlu {get_titlu(vanzare)}, gen {get_gen(vanzare)}, pret {get_pret(vanzare)}, reducere {get_reducere(vanzare)}'

