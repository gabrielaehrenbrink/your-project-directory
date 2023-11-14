import pytest
from lib.password_checker import PasswordChecker

# Test valid password
def test_password_checker():
    password = PasswordChecker()
    password = 'Gabriela123'
    assert True

# Test invalid password 

def test_invalid_password_checker():
    password_checker = PasswordChecker()
    password = '123'
    with pytest.raises(Exception) as e:
        password_checker.check(password)
    message = str(e.value)
    assert message == ("Invalid password, must be 8+ characters.")
