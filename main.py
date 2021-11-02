from Logic.crud import create
from Tests.apelare_test import test
from Tests.test_crud import test_crud
from UserInterface.console import run_ui

def main():
    vanzari = []
    vanzari = create(vanzari, '1', 'Harry Potter', 'Fantezie', 45, 'silver')
    vanzari = create(vanzari, '2', 'La rascruce de vanturi', 'Roman de dragoste', 35, 'none')
    vanzari = create(vanzari, '3', 'Moara cu noroc', 'Fictiune', 20, 'gold')
    vanzari = create(vanzari, '4', 'Ion', 'Realism', 30, 'none')
    vanzari = create(vanzari, '5', 'Descult', 'Roman', 50, 'silver')
    vanzari = run_ui(vanzari)


if __name__ == '__main__':
    test()
    main()