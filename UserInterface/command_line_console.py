from Domain.Vanzare import get_str, creeaza_vanzare
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
        undo_list = []
        redo_list = []
        print("Pentru ajutor, tastati 'help;")
        optiune = input("Dati optiunea:  ")
        task = optiune.split("; ")
        if optiune == 'stop':
            break
        for elem in task:
            comanda = elem.split(', ')
            if comanda[0].lower() == 'help':
                help()
            elif comanda[0].lower() == 'add':
                try:
                    if len(comanda) == 6:
                        if comanda[5] == 'none' or comanda[5] == 'silver' or comanda[5] == 'gold':
                            vanzari = create(vanzari, comanda[1], comanda[2], comanda[3], float(comanda[4]), comanda[5], undo_list, redo_list)
                            print("Vanzarea a fost adaugata.")
                        else:
                            print('Tip de reducere inexistent')
                    else:
                        print('Nu s-a putut adauga vanzarea: numar incorect de parametri.')
                except ValueError as ve:
                    print("Eroare : ", ve)
            elif comanda[0].lower() == 'delete':
                try:
                    if len(comanda) == 2:
                        vanzari = delete(vanzari, comanda[1], undo_list, redo_list)
                        print("Vanzarea a fost stearsa.")
                    else:
                        print('Nu s-a putut sterge vanzarea: numar incorect de parametri.')
                except ValueError as ve:
                    print("Eroare : ", ve)
            elif comanda[0].lower() == "update":
                try:
                    if len(comanda) == 6:
                        vanzari = update(vanzari, creeaza_vanzare( comanda[1], comanda[2], comanda[3], comanda[4], comanda[5]), undo_list, redo_list)
                        print("Vanzarea a fost modificata.")
                    else:
                        print('Nu s-a putut modifica vanzarea: numar incorect de parametri.')
                except ValueError as ve:
                    print("Error", ve)
            elif comanda[0].lower() == 'show_all':
                if len(comanda) == 1:
                    show_all(vanzari)
                else:
                    print('Nu s-a putut afisa lista completa de vanzari: numar incorect de parametri.')
            else:
                print("Optiune invalida! Alegeti alta sau incercati help pentru mai multe indicatii")