from example import func
import pytest


@pytest.mark.parametrize("x, result",
                         [(72, 72), (111, 16851542590), (199, 144589310.996829), (300, 1.7403083013540577e-05)])
def test_example_all(x, result):
    assert func(x) == result


def test_example_second(begin_message):
    assert func(190) == 247612715801
    print(begin_message)


def test_example_third():
    assert func(250) == 186251070.21618825

def test_example_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert func(0) == 0

