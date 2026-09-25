def validate_email(email: str) -> bool:
    return "@" in email and "." in email

def validate_phone(phone: str) -> bool:
    # TODO: add proper regex
    return len(phone) == 11 and phone.startswith("8")
