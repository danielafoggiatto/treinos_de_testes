import pytest

def test_1_soma():
    a = 1
    b = 2
    soma = a + b
    assert soma == 3
    print(soma)



def soma2(a, b):
    return a + b

def test_2_soma():
    assert soma2(3,2) == 5


@pytest.mark.parametrize("a, b, esperado", [
    (1, 2, 3),
    (5, 5, 10),
    (2, 1, 4)
])

def test_3_soma(a, b, esperado):
    assert a + b == esperado