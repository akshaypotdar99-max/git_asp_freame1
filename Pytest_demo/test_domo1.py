import pytest


@pytest.mark.smoke
def test_method1():
    print("akshay")

@pytest.mark.skip
def test_method2():
    print("potdar")

@pytest.mark.xfail
def test_method2():
    print("potdar")