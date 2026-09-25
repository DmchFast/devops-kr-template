import pytest
from validator import validate_email, validate_phone, validate_snils


def test_validate_phone_valid():
    assert validate_phone("+79161234567") is True
    assert validate_phone("89161234567") is True
    assert validate_phone("+7 (916) 123-45-67") is True
    assert validate_phone("8-916-123-45-67") is True


def test_validate_phone_invalid():
    assert validate_phone("123") is False
    assert validate_phone("+1 555 123 4567") is False
    assert validate_phone("") is False
    assert validate_phone("not a phone") is False


def test_validate_snils_valid():
    assert validate_snils("123-456-789 00") is True


def test_validate_snils_invalid():
    assert validate_snils("123") is False
