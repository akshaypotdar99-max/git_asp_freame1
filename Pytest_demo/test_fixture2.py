import pytest

@pytest.mark.usefixtures("test_fixture2")
class Test_expample2:
    def test_asp1(self, test_fixture2):
        print(test_fixture2)