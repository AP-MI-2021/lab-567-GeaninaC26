from Domain.Vanzare import get_str
from Logic.crud import create, delete, update


def help():
    print("Pentru corectitudine, structura comenzii va fi scrisa corect gramatical, cu spatiu dupa fiecare virgula/"
          ", ',' intre argumentele fiecarei comenzi si ';' intre oricare doua comenzi.")
    print("Dupa ce ati introdus corect toate functiile e care doriti sa le executati, apasati enter.")
    print("Pentru a adauga o vanzare tastati: add, id, titlu, gen, pret, reducere . Reducerea trebuie sa fie none/silver/gold.")
    print("Prentru a sterge o vanzare tastati: delete, id.")
    print("Pentru a modifica o vanzare tastati: update, id, titlu, gen, pret -> float, reducere. Reducerea trebuie sa fie none/silver/gold.")
    print("Pentru a afisa toate vanzarile tastati: show_all")
    print("Pentru a inchide meniul tastati: break.")
    print("Pentru a inchide consola, tastati: stop.")


def show_all(vanzari):
    for vanzare in vanzari:
        print(get_str(vanzare))
    print()


def meniu(vanzari):
    while True:
        print("Pentru ajutor, tastati 'help;")
        optiune = input("Dati optiunea:  ")
        task = optiune.split("; ")
        if optiune == 'stop':
            break
        for elem in task:
            comenzi = elem.split(', ')
            if comenzi[0].lower() == 'help':
                help()
            elif comenzi[0].lower() == 'add':
                try:
                    vanzari = create(vanzari, comenzi[1], comenzi[2], comenzi[3], comenzi[4], comenzi[5])
                except ValueError as ve:
                    print("Eroare : ", ve)
            elif comenzi[0].lower() == 'delete':
                try:
                    vanzari = delete(vanzari, comenzi[1])
                except ValueError as ve:
                    print("Eroare : ", ve)
            elif comenzi[0].lower() == "update":
                vanzari = update(vanzari, comenzi[1], comenzi[2], comenzi[3], comenzi[4], comenzi[5])
            elif comenzi[0].lower() == 'show_all':
                show_all(vanzari)
            else:
                print("Optiune invalida! Alegeti alta sau incercati help pentru mai multe indicatii")