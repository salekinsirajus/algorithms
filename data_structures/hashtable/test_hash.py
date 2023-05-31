from hash import Hash

def test_insert():
    h = Hash()
    h[1] = 10
    assert h[1] == 10

def test_search():
    h = Hash()
    h[1] = 10

    assert(1 in h)

def test_collision():
    h = Hash()
    h[10] = 10
    h[110] = 110

    assert h[10] == 10
    assert h[110] == 110


if __name__ == '__main__':
    test_insert()
    test_search()
    test_collision()
