import random
import secrets
import string


PASSWORD_LENGTH = 6

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SPECIAL = "!@#$%^&*"

ALL_SYMBOLS = LOWERCASE + UPPERCASE + DIGITS + SPECIAL


def generate_password() -> str:
    password_characters = [
        secrets.choice(LOWERCASE),
        secrets.choice(UPPERCASE),
        secrets.choice(DIGITS),
        secrets.choice(SPECIAL),
    ]

    remaining_length = PASSWORD_LENGTH - len(password_characters)

    password_characters.extend(
        secrets.choice(ALL_SYMBOLS)
        for _ in range(remaining_length)
    )

    random.shuffle(password_characters)

    return "".join(password_characters)