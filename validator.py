import re


def validate_email(email: str) -> bool:
    """Проверяет корректность email-адреса."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Проверяет корректность российского номера телефона."""
    pattern = r'^(\+7|8)[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}$'
    return bool(re.match(pattern, phone))


def validate_snils(snils: str) -> bool:
    """Проверяет корректность СНИЛС."""
    pattern = r'^\d{3}-\d{3}-\d{3} \d{2}$'
    return bool(re.match(pattern, snils))
