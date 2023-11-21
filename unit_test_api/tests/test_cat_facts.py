from unittest.mock import Mock
from lib.cat_facts_challenge import CatFacts

def test_cat_facts_provided():
    requester_mock = Mock()
    response_mock = Mock()
    response_mock.text = "Cat fact: A cat will tremble or shiver when it is extreme pain."
    response_mock.json.return_value = {"fact": "A cat will tremble or shiver when it is extreme pain."}
    requester_mock.get.return_value = response_mock

    cat_facts = CatFacts(requester_mock)
    assert cat_facts.provide() == "Cat fact: A cat will tremble or shiver when it is extreme pain."