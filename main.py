from Logic.crud import create, generare
from Tests.apelare_test import test
from Tests.test_crud import test_crud
from UserInterface.command_line_console import meniu
from UserInterface.console import run_ui

def main():
    vanzari = []
    undo_list = []
    redo_list = []
    vanzari = create(vanzari, '1', 'Harry Potter', 'Fictiune', 45, 'silver', undo_list, redo_list)
    vanzari = create(vanzari, '2', 'La rascruce de vanturi', 'Roman', 35, 'none', undo_list, redo_list)
    vanzari = create(vanzari, '3', 'Moara cu noroc', 'Fictiune', 20, 'gold', undo_list, redo_list)
    vanzari = create(vanzari, '4', 'Ion', 'Realism', 30, 'none', undo_list, redo_list)
    vanzari = create(vanzari, '5', 'Descult', 'Roman', 50, 'silver', undo_list, redo_list)
    vanzari = run_ui(vanzari, undo_list, redo_list)

if __name__ == '__main__':
    test()
    main()