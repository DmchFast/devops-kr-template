from validator import validate_phone

def test_phone_valid():
    assert validate_phone("89991234567") is True
