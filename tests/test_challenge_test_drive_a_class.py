from lib.challenge_test_drive_a_class import *

def test_check():
    grammar = GrammarStats()
    result = grammar.check('This is good grammar.')
    assert result == True


def test_false_check():
    grammar = GrammarStats()
    result = grammar.check('this is not good grammar.')
    assert result == False

def test_question_check():
    grammar = GrammarStats()
    result = grammar.check('Is this good grammar?')
    assert result == True

def test_percentage_good():
    grammar = GrammarStats()
    result = grammar.percentage_good()
    assert result == 0


    grammar.check('This is good grammar.')
    grammar.check('this is not good grammar.')
    grammar.check('Is this good grammar?')

    result = grammar.percentage_good()
    assert result == 66