import calculator_logic as calc_log
import pytest

def test_add():
    assert calc_log.add(5, 5) == 10
    assert calc_log.add(-1, 1) == 0
    assert calc_log.add(-2, -2) == -4

    with pytest.raises(TypeError):
        calc_log.add('text', 7)
    with pytest.raises(TypeError):
        calc_log.add(7,'text')


def test_subtract():
    assert calc_log.subtract(4, 2) == 2
    assert calc_log.subtract(-3, 1) == -4
    assert calc_log.subtract(-5, -5) == 0

    with pytest.raises(TypeError):
        calc_log.subtract('text', 7)
    with pytest.raises(TypeError):
        calc_log.subtract(7,'7')


def test_multiply():
    assert calc_log.multiply(2, 2) == 4
    assert calc_log.multiply(-3, 5) == -15
    assert calc_log.multiply(-5, -5) == 25


def test_divide():
    assert calc_log.divide(10, 5) == 2
    assert calc_log.divide(-4, 2) == -2
    assert calc_log.divide(-50, -10) == 5

    with pytest.raises(TypeError):
        calc_log.divide('text', 7)
    with pytest.raises(TypeError):
        calc_log.divide(7, '7')

    with pytest.raises(ZeroDivisionError):
        calc_log.divide(7, 0)


test_add()
test_subtract()
test_multiply()
test_divide()
print('Тесты пройдены успешно')

