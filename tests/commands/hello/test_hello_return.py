# Import libraries and necessaries utils

import pytest
from utils.commands.hello.cHello import HelloCommand
from utils.jsonImporting.jsonimport import readJSON

# Load translations

translations = readJSON()

# Load test parameters

@pytest.mark.parametrize("expected", [
    ("hello"),
])

def test_hello_return(expected):
    
    input_value = HelloCommand()

    actual_expected = translations["command"][expected]

    if input_value == actual_expected:
        return True
    else:
        return False