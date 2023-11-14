from lib.design_function_two import writting_skills

# given a test with lower case and no full stop, resturn a string with first letter upper case and full stop at the end
def test_lower_case_string():
    test_string = writting_skills('this is all lower case')
    assert test_string == 'This is all lower case.'


# given a test with lower case and question word, return a string with first letter upper case and question mark at the end
def test_question_mark_string():
    test_string = writting_skills('what is this string')
    assert test_string == 'What is this string?'


# given a test with all upper case, return a string with just first letter upper case and exclamation at the end
def test_exclamation_string():
    test_string = writting_skills('THIS IS ALL UPPER CASE')
    assert test_string == 'This is all upper case!'