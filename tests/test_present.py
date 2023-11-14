import pytest
from lib.present import Present

#  When we wrap an item we get it back when unwrapping

def test_wrap_and_unwrap():
    present = Present()
    present.wrap(10)
    assert present.unwrap() == 10

# If we unwrap before wrapping we get an error message

def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message = str(e.value)
    assert message == ("No contents have been wrapped.")


# If we wrap something that has already been wrapped 

def test_wrap_already_wrapped():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    message = str(e.value)
    assert message == ("A contents has already been wrapped.")