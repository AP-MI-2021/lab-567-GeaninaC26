from Logic.crud import create
from UserInterface.console import handle_undo, handle_redo


def test_undo_redo():
    vanzari=[]
    undo_list=[]
    redo_list=[]
    vanzari = create(vanzari, '1', 'Harry Potter', 'Fictiune', 45, 'silver', undo_list, redo_list)
    assert len(vanzari) == 1
    vanzari = create(vanzari, '2', 'La rascruce de vanturi', 'Roman', 35, 'none', undo_list, redo_list)
    assert len(vanzari) == 2
    vanzari = create(vanzari, '3', 'Moara cu noroc', 'Fictiune', 20, 'gold', undo_list, redo_list)
    assert len(vanzari) == 3
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 2
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 1
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 0
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 0
    vanzari = create(vanzari, '1', 'Harry Potter', 'Fictiune', 45, 'silver', undo_list, redo_list)
    vanzari = create(vanzari, '2', 'La rascruce de vanturi', 'Roman', 35, 'none', undo_list, redo_list)
    vanzari = create(vanzari, '3', 'Moara cu noroc', 'Fictiune', 20, 'gold', undo_list, redo_list)
    assert len(vanzari) == 3
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 3
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 2
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 1
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 2
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 3
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 2
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 1
    vanzari = create(vanzari, '4', 'Ion', 'Realism', 30, 'none', undo_list, redo_list)
    assert len(vanzari) == 2
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 2
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 1
    vanzari = handle_undo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 0
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 1
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 2
    vanzari = handle_redo(vanzari, undo_list, redo_list)
    assert len(vanzari) == 2