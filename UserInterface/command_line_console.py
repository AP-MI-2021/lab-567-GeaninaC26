from Domain.Vanzare import creeaza_vanzare, get_str
from Logic.crud import create, delete


def program(vanzari):
    print("Scrie 'help' pentru ajutor.")
    while (optiune := input()) != 'quit':
        if optiune == 'help':
            print("Pentru a adauga o vanzare scrie 'add' 'id' 'titlu' 'gen' 'pret' 'reducere'.")
            print("Pentru a sterge o vanzare scrie 'delete' 'id'")
            print("Pentru a afisa toate vanzarile scrie 'show_all'")
        else:
            option = optiune.split(' ')
            if option[0] == 'add':
                try:
                    if len(option) != 6:
                        print("Optiune nevalida.")
                    else:
                        create(vanzari,option[1],option[2],option[3],option[4],option[5])
                except KeyError as k:
                    print("eroare", k)
            elif option == 'delete':
                try:
                    if len(option) != 2:
                        print("Optiune nevalida.")
                    else:
                        delete(vanzari, option[1])
                except KeyError as k:
                    print("Eroare", k)
            elif option == 'show_all':
                try:
                    if len(option) != 1:
                        print("Optiune nevalida")
                    else:
                        for vanzare in vanzari:
                            print(get_str(vanzare))
                except KeyError as k:
                    print("Eroare:" , k)

