import pytest
@pytest.fixture()
def test_fixture1():
    print("this is test fixture1")
    yield
    print("This is tear down method")


@pytest.fixture()
def test_fixture2():
    print("this is test fixture2")
    return ["Name","akshay","potdar"]

@pytest.fixture(params=["Admin","Stanadard","Downloader"])
def test_user(request):
    return request.param

@pytest.fixture(params=[("Admin","Asset1","ID1"),("Stanadard","Asset2","ID2"),("Downloader","Asset3","ID3")])
def test_user_info(request):
    return request.param


