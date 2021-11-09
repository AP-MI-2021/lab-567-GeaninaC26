from Domain.Vanzare import get_str, get_titlu, get_reducere, get_pret, get_gen, creeaza_vanzare
from Logic.crud import create, read, update, delete
from UserInterface.command_line_console import meniu
from Logic.functionalitati import aplicare_discount, modificare_gen, determinare_pret_minim, sortare_in_functie_de_pret, nr_titluri_distincte_pe_gen, do_undo, do_redo
def show_menu():
    print("cd. Command Line Console")
    print("1. CRUD")
    print("2. Aplicare dicount.")
    print("3. Modifica genul cartii daca are un titlu dat.")
    print("4. Determinarea pretului minim pentru fiecare gen.")
    print("5. Ordonarea vanzarilor crescator dupa pret.")
    print("6. Afișarea numărului de titluri distincte pentru fiecare gen.")
    print("a. Afiseaza vanzarile.")
    print("u. Undo.")
    print("r. Redo.")
    print("x. Iesire")


def handle_add(vanzari, undo_list, redo_list):
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
        return create(vanzari, id, titlu, gen, pret, reducere, undo_list, redo_list)
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



def handle_update(vanzari, undo_list, redo_list):
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
        return update(vanzari, new_vanzare, undo_list, redo_list)
    except ValueError as ve:
        print("Eroare", ve)
    return vanzari


def handle_delete(vanzari, undo_list, redo_list):
    """
    Sterge din lista de vanzari, vanzarea cu id-ul dat de utilizator
    :param vanzari:
    :return:
    """
    try:
        id_vanzare = input('Dati id-ul vanzarii care se va sterge:')
        return delete(vanzari, id_vanzare, undo_list, redo_list)
    except ValueError as ve:
        print("Eroare ", ve)
    return vanzari


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

def handle_crud(vanzari, undo_list, redo_list):
    while True:
        print('1.Adaugare vanzare.')
        print('2.Modificare vanzare.')
        print('3.Stergere vanzare.')
        print('a.Afisare vanzari.')
        print('d.Detaliile vanzarii.')
        print('b.Revenire.')
        optiune = input('Alegeti o optiune: ')
        if optiune == '1':
            vanzari = handle_add(vanzari, undo_list, redo_list)
        elif optiune == '2':
            vanzari = handle_update(vanzari, undo_list, redo_list)
        elif optiune == '3':
            vanzari = handle_delete(vanzari, undo_list, redo_list)
        elif optiune == 'a':
            handle_show_all(vanzari)
        elif optiune == 'd':
            handle_show_details(vanzari)
        elif optiune == 'b':
            break
        else:
            print('Optiune nevalida.')
    return vanzari

def handle_discount(vanzari, undo_list, redo_list):
    """
    Aplica discount-urile silver si gold pe toate vanzarile din lista.
    :param vanzari:
    :return:
    """
    return aplicare_discount(vanzari, undo_list, redo_list)


def handle_change_genre(vanzari, undo_list, redo_list):
    """
    Modifica genul vanzarii cu titlul dat de utilizator, cu un nou gen, dat de utilizator
    :param vanzari:
    :return:
    """
    titlu = input("Dati titlul cartii al carui gen doriti sa il modificati: ")
    gen_nou = input("Dati genul cu care se va inlocui genul initial al vanzarii cu titlul 'titlu': ")
    return modificare_gen(vanzari, titlu, gen_nou, undo_list, redo_list)


def handle_min_price(vanzari):
    rezultat = determinare_pret_minim(vanzari)
    for cheie in rezultat:
        print(cheie, ":", rezultat[cheie], "lei")
    return vanzari


def handle_ordonare_in_functie_de_pret(vanzari, undo_list, redo_list):
    '''
    Functie care modifica lista de vanzari ordonand-o crescator in functie de pret
    :param lista: lista de vanzari
    :return: lista ordonata crescator in functie de pret
    '''
    vanzari = sortare_in_functie_de_pret(vanzari, undo_list, redo_list)
    return vanzari


def handle_nr_titluri_distincte_per_gen(vanzari):
    '''
    Functie care determina numarul de titluri distincte pentru fiecare gen
    :param lista: lista de vanzari
    :return: lista de vanzari
    '''
    rezultat = nr_titluri_distincte_pe_gen(vanzari)

    for cheie in rezultat:
        print(cheie, ":", rezultat[cheie], "titluri distincte")

    return vanzari


def handle_undo(vanzari,undo_list,redo_list):
    undo_result=do_undo(undo_list,redo_list)
    if undo_result is not None:
        return undo_result
    return vanzari


def handle_redo(vanzari,undo_list,redo_list):
    redo_result = do_redo(undo_list, redo_list)
    if redo_result is not None:
        return redo_result
    return vanzari


def run_ui(vanzari, undo_list, redo_list):
    while True:
        show_menu()
        optiune = input('Alegeti o optiune')
        if optiune == '1':
            vanzari = handle_crud(vanzari, undo_list, redo_list)
        elif optiune == '2':
            vanzari = handle_discount(vanzari, undo_list, redo_list)
            print("Discount-urile au fost aplicate. Pentru verificare tastati 'a'.")
        elif optiune == '3':
            vanzari = handle_change_genre(vanzari, undo_list, redo_list)
        elif optiune == '4':
            print("Genurile si preturile minime pentru fiecare gen: ")
            vanzari = handle_min_price(vanzari)
        elif optiune == '5':
            vanzari = handle_ordonare_in_functie_de_pret(vanzari, undo_list, redo_list)
            print("Vanzarile au fost ordonate. Pentru verificare tastati 'a'.")
        elif optiune == '6':
            print("Genurile si numarul de titluri distincte pentru fiecare gen: ")
            vanzari = handle_nr_titluri_distincte_per_gen(vanzari)
        elif optiune == 'a':
            handle_show_all(vanzari)
        elif optiune  == 'x':
            break
        elif optiune == 'cd':
            meniu(vanzari)
        elif optiune == 'u':
            vanzari = handle_undo(vanzari, undo_list, redo_list)
        elif optiune == 'r':
            vanzari = handle_redo(vanzari, undo_list, redo_list)
        else:
            print('Optiune nevalida.')
    return vanzari
