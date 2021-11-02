from Domain.Vanzare import get_str, get_titlu, get_reducere, get_pret, get_gen, creeaza_vanzare
from Logic.crud import create, read, update, delete
from Logic.functionalitati import aplicare_discount, modificare_gen


def show_menu():
    print("1. CRUD")
    print("2. Aplicare dicount.")
    print("3. Modifica genul cartii daca are un titlu dat.")
    print("4. Determinarea pretului minim pentru fiecare gen.")
    print("5. Ordonarea vanzarilor crescator dupa pret.")
    print("6. Afișarea numărului de titluri distincte pentru fiecare gen.")
    print("a. Afiseaza vanzarile.")
    print("x. Iesire")


def handle_add(vanzari):
    """
    Adauga in lista de vanzari o vanzare creata de utilizator.
    :param vanzari: lista de vanzari
    :return:
    """
    try:
        id = input("Dati id: ")
        titlu = input("Dati titlu: ")
        gen = input("Dati gen: ")
        pret = float(input("Dati pretul: "))
        reducere = input("Dati reducere: ")
        return create(vanzari, id, titlu, gen, pret, reducere)
    except ValueError as ve:
        print("Eroare: ", ve)
    return vanzari


def handle_show_all(vanzari):
    """
    Afiseaza lista de vanzari
    :param vanzari: lista de vanzari
    :return:
    """
    for vanzare in vanzari:
        print(get_str(vanzare))



def handle_update(vanzari):
    """
    Actualizeaza detaliile unei vanzari al carui id este dat de utilizator.
    :param vanzari:
    :return:
    """
    try:
        id = input("Dati id-ul vanzarii care se actualizeaza:  ")
        titlu = input("Dati noul titlu: ")
        gen = input("Dati  noul gen: ")
        pret = float(input("Dati noul pret: "))
        reducere = input("Dati noua reducere: ")
        new_vanzare = creeaza_vanzare(id,titlu,gen, pret, reducere)
        return update(vanzari, new_vanzare)
    except ValueError as ve:
        print("Eroare", ve)


def handle_delete(vanzari):
    """
    Sterge din lista de vanzari, vanzarea cu id-ul dat de utilizator
    :param vanzari:
    :return:
    """
    try:
        id_vanzare = input('Dati id-ul vanzarii care se va sterge:')
        return delete(vanzari, id_vanzare)
    except ValueError as ve:
        print("Eroare ", ve)


def handle_show_details(vanzari):
    """
    Afiseaza detaliile vanzarii cu un id dat de utilizator
    :param vanzari: lista de vanzari
    :return:
    """
    id_vanzare = input('Dati id-ul vanzarii: ')
    vanzare = read(vanzari, id_vanzare)
    if vanzare is None:
        print("Vanzare inexistenta.")
    else:
        print(f'Titlu: {get_titlu(vanzare)}')
        print(f'Gen: {get_gen(vanzare)}')
        print(f'Pret: {get_pret(vanzare)}')
        print(f'Reducere: {get_reducere(vanzare)}')

def handle_crud(vanzari):
    while True:
        print('1.Adaugare vanzare.')
        print('2.Modificare vanzare.')
        print('3.Stergere vanzare.')
        print('a.Afisare vanzari.')
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

def handle_discount(vanzari):
    """
    Aplica discount-urile silver si gold pe toate vanzarile din lista.
    :param vanzari:
    :return:
    """
    return aplicare_discount(vanzari)


def handle_change_genre(vanzari):
    """
    Modifica genul vanzarii cu titlul dat de utilizator, cu un nou gen, dat de utilizator
    :param vanzari:
    :return:
    """
    titlu = input("Dati titlul cartii al carui gen doriti sa il modificati: ")
    gen_nou = input("Dati genul cu care se va inlocui genul initial al vanzarii cu titlul 'titlu': ")
    return modificare_gen(vanzari, titlu, gen_nou)



def run_ui(vanzari):
    while True:
        show_menu()
        optiune = input('Alegeti o optiune')
        if optiune == '1':
            vanzari = handle_crud(vanzari)
        elif optiune == '2':
            vanzari = handle_discount(vanzari)
        elif optiune == '3':
            vanzari = handle_change_genre(vanzari)
        elif optiune  == 'x':
            break
        else:
            print('Optiune nevalida.')
    return vanzari
