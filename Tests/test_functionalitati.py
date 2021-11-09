from Domain.Vanzare import creeaza_vanzare, get_pret, get_gen, get_id
from Logic.crud import generare
from Logic.functionalitati import aplicare_discount, modificare_gen, determinare_pret_minim, sortare_in_functie_de_pret, nr_titluri_distincte_pe_gen


def test_aplicare_discount():

    vanzare1 = creeaza_vanzare("1", "Harry Potter", "fictiune fantastica", 50, "silver")
    vanzare2 = creeaza_vanzare("2", "La rascruce de vanturi", "roman", 45, "gold")
    lista = []
    lista.append(vanzare1)
    lista.append(vanzare2)
    aplicare_discount(lista, [], [])

    assert get_pret(lista[0]) == 47.5
    assert get_pret(lista[1]) == 40.5


def test_modificare_gen():
    vanzare1 = creeaza_vanzare("1", "Harry Potter", "fictiune fantastica", 50, "silver")
    vanzare2 = creeaza_vanzare("2", "La rascruce de vanturi", "roman", 45, "gold")

    lst_vanzari = []
    lst_vanzari.append(vanzare1)
    lst_vanzari.append(vanzare2)
    modificare_gen(lst_vanzari, "Harry Potter", "actiune", [], [])
    assert get_gen(lst_vanzari[0]) == "actiune"


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