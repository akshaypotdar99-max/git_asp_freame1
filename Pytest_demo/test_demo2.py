import pytest


@pytest.mark.smoke
def test_method3():
    a = "hi"
    assert a=="hello", "text not matching"