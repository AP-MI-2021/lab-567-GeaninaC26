from Domain.Vanzare import get_str, get_titlu, get_reducere, get_pret, get_gen, creeaza_vanzare
from Logic.crud import create, read, update, delete


def show_menu():
    print("1. CRUD")
    print("2. Aplicare dicount.")
    print("3. Modifica vanzare")
    print("4. Modifica genul cartii daca are un titlu dat")
    print("a. Afiseaza vanzarile")
    print("x. Iesire")


def handle_add(vanzari):
    id = input("Dati id: ")
    titlu = input("Dati titlu: ")
    gen = input("Dati gen: ")
    pret = float(input("Dati pretul: "))
    reducere = input("Dati reducere: ")
    return create(vanzari, id, titlu, gen, pret, reducere)


def handle_show_all(vanzari):
    for vanzare in vanzari:
        print(get_str(vanzare))


def handle_show_details(vanzari):
    id_vanzare = int(input('Dati id-ul vanzarii: '))
    vanzare = read(vanzari, id_vanzare)
    print(f'Titlu: {get_titlu(vanzare)}')
    print(f'Gen: {get_gen(vanzare)}')
    print(f'Pret: {get_pret(vanzare)}')
    print(f'Reducere: {get_reducere(vanzare)}')


def handle_update(vanzari):
    id = input("Dati id-ul vanzarii care se actualizeaza:  ")
    titlu = input("Dati noul titlu: ")
    gen = input("Dati  noul gen: ")
    pret = float(input("Dati noul pret: "))
    reducere = input("Dati noua reducere: ")
    return update(vanzari, creeaza_vanzare(id,titlu,gen,pret,reducere))


def handle_delete(vanzari):
    id_vanzare = int(input('Dati id-ul vanzarii care se va sterge:'))
    return delete(vanzari, id_vanzare)


def handle_crud(vanzari):
    while True:
        print('1.Adaugare vanzare.')
        print('2.Modificare vanzare.')
        print('3.Stergere vanzare.')
        print('a.Afisare vanzare.')
        print('d.Detaliile vanzarii.')
        print('b.Revenire.')
        optiune = input('Alegeti o optiune: ')
        if optiune == '1':
            vanzari = handle_add(vanzari)
        elif optiune == '2':
            vanzari = handle_update(vanzari)
        elif optiune == '3':
            vanzari = handle_delete(vanzari)
        elif optiune == 'a':
            handle_show_all(vanzari)
        elif optiune == 'd':
            handle_show_details(vanzari)
        elif optiune == 'b':
            break
        else:
            print('Optiune nevalida.')
    return vanzari


def run_ui(vanzari):
    while True:
        show_menu()
        optiune = input('Alegeti o optiune')
        if optiune == '1':
            vanzari = handle_crud(vanzari)
        elif optiune  == 'x':
            break
        else:
            print('Optiune nevalida.')
    return vanzari
