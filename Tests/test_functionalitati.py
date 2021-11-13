from Domain.Vanzare import creeaza_vanzare, get_pret, get_gen, get_id, get_titlu, get_reducere
from Logic.crud import generare
from Logic.functionalitati import aplicare_discount, modificare_gen, determinare_pret_minim, sortare_in_functie_de_pret, nr_titluri_distincte_pe_gen


def test_aplicare_discount():

    vanzari = generare()
    new_vanzari = aplicare_discount(vanzari, [], [])
    for index in range(0, len(vanzari)):
        if get_reducere(vanzari[index]) != 'none':
            assert get_pret(vanzari[index]) != get_pret(new_vanzari[index])


def test_modificare_gen():
    vanzari = generare()
    new_vanzari = modificare_gen(vanzari, "Harry Potter", "actiune", [], [])
    for index in range(0, len(vanzari)):
        if get_titlu(vanzari[index]) == "Harry Potter":
            assert get_gen(vanzari[index]) != get_gen(new_vanzari[index])


def test_determina_pret_minim():
    lista = generare()
    rezultat = determinare_pret_minim(lista)

    assert rezultat["Fictiune"] == 20
    assert rezultat["Roman"] == 35
    assert rezultat["Realism"] == 30

def test_sortare_in_functie_de_pret():
    lista = generare()
    lista = sortare_in_functie_de_pret(lista, [], [])
    assert get_id(lista[0]) == "3"
    assert get_pret(lista[0]) < get_pret(lista[1])
    assert get_id(lista[1]) == "4"


def test_nr_titluri_distincte_pe_gen():
    lista = generare()
    rezultat = nr_titluri_distincte_pe_gen(lista)
    assert rezultat["Fictiune"] == 2
    assert rezultat["Roman"] == 2
    assert rezultat["Realism"] == 1


def test_all():
    test_aplicare_discount()
    test_modificare_gen()
    test_determina_pret_minim()
    test_sortare_in_functie_de_pret()
    test_nr_titluri_distincte_pe_gen()