from Domain.Vanzare import get_id, get_pret, get_gen, get_titlu
from Logic.crud import create
from Logic.functionalitati import do_undo, do_redo, sortare_in_functie_de_pret, modificare_gen, aplicare_discount
from UserInterface.console import handle_undo, handle_redo


def test_undo_redo():
    vanzari=[]
    undo_list=[]
    redo_list=[]
    vanzari = create(vanzari, '1', 'Harry Potter', 'Fictiune', 45, 'silver', undo_list, redo_list)
    assert len(vanzari) == 1
    assert get_titlu(vanzari[0]) == 'Harry Potter'
    vanzari = create(vanzari, '2', 'La rascruce de vanturi', 'Roman', 35, 'none', undo_list, redo_list)
    assert len(vanzari) == 2
    assert get_titlu(vanzari[1]) == 'La rascruce de vanturi'
    vanzari = create(vanzari, '3', 'Moara cu noroc', 'Fictiune', 20, 'gold', undo_list, redo_list)
    assert len(vanzari) == 3
    assert get_titlu(vanzari[2]) == 'Moara cu noroc'
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 2
    assert get_titlu(vanzari[0]) == 'Harry Potter'
    assert get_titlu(vanzari[1]) == 'La rascruce de vanturi'
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 1
    assert get_titlu(vanzari[0]) == 'Harry Potter'
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 0
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 0
    vanzari = create(vanzari, '1', 'Harry Potter', 'Fictiune', 45, 'silver', undo_list, redo_list)
    vanzari = create(vanzari, '2', 'La rascruce de vanturi', 'Roman', 35, 'none', undo_list, redo_list)
    vanzari = create(vanzari, '3', 'Moara cu noroc', 'Fictiune', 20, 'gold', undo_list, redo_list)
    assert len(vanzari) == 3
    assert get_titlu(vanzari[0]) == 'Harry Potter'
    assert get_titlu(vanzari[1]) == 'La rascruce de vanturi'
    assert get_titlu(vanzari[2]) == 'Moara cu noroc'
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 3
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 2
    assert get_titlu(vanzari[0]) == 'Harry Potter'
    assert get_titlu(vanzari[1]) == 'La rascruce de vanturi'
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 1
    assert get_titlu(vanzari[0]) == 'Harry Potter'
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 2
    assert get_titlu(vanzari[0]) == 'Harry Potter'
    assert get_titlu(vanzari[1]) == 'La rascruce de vanturi'
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 3
    assert get_titlu(vanzari[0]) == 'Harry Potter'
    assert get_titlu(vanzari[1]) == 'La rascruce de vanturi'
    assert get_titlu(vanzari[2]) == 'Moara cu noroc'
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 2
    assert get_titlu(vanzari[0]) == 'Harry Potter'
    assert get_titlu(vanzari[1]) == 'La rascruce de vanturi'
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 1
    assert get_titlu(vanzari[0]) == 'Harry Potter'
    vanzari = create(vanzari, '4', 'Ion', 'Realism', 30, 'none', undo_list, redo_list)
    assert len(vanzari) == 2
    assert get_id(vanzari[0]) == '1'
    assert get_id(vanzari[1]) == '4'
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 2
    assert get_id(vanzari[0]) == '1'
    assert get_id(vanzari[1]) == '4'
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 1
    assert get_id(vanzari[0]) == '1'
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 0
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 1
    assert get_id(vanzari[0]) == '1'
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 2
    assert get_id(vanzari[0]) == '1'
    assert get_id(vanzari[1]) == '4'
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 2
    assert get_id(vanzari[0]) == '1'
    assert get_id(vanzari[1]) == '4'
    vanzari = sortare_in_functie_de_pret(vanzari, undo_list, redo_list)
    assert get_id(vanzari[0]) == '4'
    assert get_pret(vanzari[0]) == 30
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert get_id(vanzari[0]) == '1'
    assert get_pret(vanzari[0]) == 45
    vanzari = aplicare_discount(vanzari, undo_list, redo_list)
    assert get_pret(vanzari[0]) == 42.75
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert get_pret(vanzari[0]) == 45
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert get_pret(vanzari[0]) == 42.75
    vanzari = modificare_gen(vanzari, 'Harry Potter', 'Drama', undo_list, redo_list)
    assert get_gen(vanzari[0]) == 'Drama'
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert get_gen(vanzari[0]) == 'Fictiune'
