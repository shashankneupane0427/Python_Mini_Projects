import re

def validate_name(name):
    return len(name.strip()) > 2

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def validate_password(password):
    return (
        len(password) > 8 and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password)
    )
