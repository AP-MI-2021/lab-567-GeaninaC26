from Domain.Vanzare import creeaza_vanzare, get_pret, get_gen
from Logic.functionalitati import aplicare_discount, modificare_gen


def test_aplicare_discount():

    vanzare1 = creeaza_vanzare("1", "Harry Potter", "fictiune fantastica", 50, "silver")
    vanzare2 = creeaza_vanzare("2", "La rascruce de vanturi", "roman", 45, "gold")
    lista = []
    lista.append(vanzare1)
    lista.append(vanzare2)
    aplicare_discount(lista)

    assert get_pret(lista[0]) == 47.5
    assert get_pret(lista[1]) == 40.5


def test_modificare_gen():
    vanzare1 = creeaza_vanzare("1", "Harry Potter", "fictiune fantastica", 50, "silver")
    vanzare2 = creeaza_vanzare("2", "La rascruce de vanturi", "roman", 45, "gold")

    lst_vanzari = []
    lst_vanzari.append(vanzare1)
    lst_vanzari.append(vanzare2)
    modificare_gen(lst_vanzari, "Harry Potter", "actiune")
    assert get_gen(lst_vanzari[0]) == "actiune"

def test_all():
    test_aplicare_discount()
    test_modificare_gen()