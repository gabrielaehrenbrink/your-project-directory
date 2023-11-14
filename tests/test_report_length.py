from lib.report_length import *

def test_report_length_2_():
    result = report_length("aa")
    assert result == "This string was 2 characters long."


def test_report_length_10_():
    result = report_length("1234567891")
    assert result == "This string was 10 characters long."


def test_report_length_23_():
    result = report_length("12345678901234567890123")
    assert result == "This string was 23 characters long."