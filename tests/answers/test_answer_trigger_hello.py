import pytest
from unittest.mock import patch
from utils.answers.answers import answers
from utils.jsonImporting.jsonimport import readJSON

translations = readJSON()
@pytest.mark.parametrize("user_input, expected", [
    ("Hello", "hello"),
    ("Hello Artemis", "hello"),
    ("Hello Assistant", "hello"),
]) 

def test_trigger_hello(user_input, expected):
    with patch('utils.answers.answers.say') as mock_say:

        answers(user_input)

        actual_expected = translations["command"]["hello"]
        mock_say.assert_called_with(actual_expected) 