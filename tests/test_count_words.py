from lib.count_words import *

def test_count_words():
    count = count_words('This is three')
    assert count == f'This string has 3 words'

def test_count_words_multiple_spaces():
    count = count_words("This  is   three")
    assert count == f'This string has 3 words'