import pytest

def wont_work(x):
    return x / 0

def test_wont_work():
    with pytest.raises(ZeroDivisionError):
        wont_work(1)
