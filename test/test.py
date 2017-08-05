def setUp():
    print ("Start Test")

def tearDown():
    print ("End Test")

def test1():
    print ("test_fun1")
    assert 2 + 3 == 5

def test2():
    print ("test_fun2")
    assert 1 + 1 != 3
