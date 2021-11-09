from Domain.Vanzare import creeaza_vanzare, get_id
from Logic.crud import create, read, update, delete

def get_data():
    return [
        creeaza_vanzare(1, 'Morometii', 'Roman', 35, 'silver'),
        creeaza_vanzare(2, 'Moara cu noroc', 'Nuvela', 40, 'none'),
        creeaza_vanzare(3, 'Poezii', 'Lirica', 20, 'gold'),
        creeaza_vanzare(4, 'Harap Alb', 'Basm', 35, 'none'),
    ]

def test_create():
    vanzari = get_data()
    params = (5, 'Franklin', 'Copii', 43, 'none',[], [])
    vn= creeaza_vanzare(*params[:-2])
    new_vanzari = create(vanzari, *params )
    assert len(new_vanzari) == len(vanzari) + 1
    assert vn in new_vanzari

    #testam daca se lanseaza exceptie pt id duplicat
    params2 = (5, 'Franklin', 'Copii', 43, 'none', [], [])
    try:
        _ = create(new_vanzari, *params2)
        assert False
    except ValueError:
        assert True


def test_read():
    vanzari = get_data()
    some_v = vanzari[2]
    assert read(vanzari, get_id(some_v)) == some_v
    assert read(vanzari, None) == vanzari


def test_update():
    vanzari = get_data()
    v_updated = creeaza_vanzare(2, 'Geronimo Stilton', 'Copii', 60, 'gold')
    updated = update(vanzari, v_updated, [], [])
    assert v_updated in updated
    assert v_updated not in vanzari
    assert len(updated) == len(vanzari)


def test_delete():
    vanzari = get_data()
    to_delete = 3
    v_deleted = read(vanzari, to_delete)
    deleted = delete(vanzari,to_delete, [], [])
    assert v_deleted not in deleted
    assert v_deleted in vanzari
    assert len(deleted) == len(vanzari) - 1


def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()