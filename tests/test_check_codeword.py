from lib.check_codeword import *

def test_check_incorrect_codeword():
    result = check_codeword("Helicopter")
    assert result == "WRONG!"

def test_check_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct!, come in."

def test_check_almost_codeword():
    result = check_codeword("house")
    assert result == "Close, but nope."


