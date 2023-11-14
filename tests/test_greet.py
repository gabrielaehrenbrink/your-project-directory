from lib.greet import *

def test_greet():
    result = greet("Ana")
    assert result == "Hello, Ana!"