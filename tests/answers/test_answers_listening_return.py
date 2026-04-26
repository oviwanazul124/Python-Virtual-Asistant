from utils.answers.answers import answers

def test_answers():
    assert answers("Hello") == True
    assert answers("ghuidferafdgui") == True
    assert answers(" Hello ") == True
