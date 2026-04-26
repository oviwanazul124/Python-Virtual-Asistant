# Import needed libraries and utils for the test

import pytest
from unittest.mock import patch
from utils.answers.answers import answers

# Start the parameters for the test
@pytest.mark.parametrize("user_input, expected", [
    ("Wikipedia minecraft", "Wikipedia minecraft"),
    ("Wikipedia THISISATEST", "Wikipedia THISISATEST"),
    ("Wikipedia 324980324809234890234", "Wikipedia 324980324809234890234"),
    ("Wikipedia /.@#~€¬", "Wikipedia /.@#~€¬"),
    ("Wikipedia CH1o234Ea", "Wikipedia CH1o234Ea")
])

def test_trigger_wikipedia(user_input, expected):
    with patch('utils.answers.answers.wikipediaSearch') as mock_wikipedia:
        
        answers(user_input)
        mock_wikipedia.assert_called_with(expected)