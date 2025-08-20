
def test_newmethod1(test_fixture1):
    print("this is new method 1")

def test_newmethod2(test_user):
    print(f"This user is {test_user}")

def test_newmethod3(test_user_info):
    print(f"This user is {test_user_info[0]} having asset {test_user_info[1]} and asset ID is {test_user_info[2]}")
