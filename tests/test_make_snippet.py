from lib.make_snippet import *

def test_make_snippet():
    new_string = make_snippet('This is three.')
    assert new_string == 'This is three.'
    

def test_make_snippet_more_5():
    new_string = make_snippet("This is a very very very long string")
    assert new_string == "This is a very very..."


