import secrets
import string

from .models import ShortURL

ALPHABET = string.ascii_letters + string.digits
CODE_LENGTH = 7


def generate_code(length=CODE_LENGTH):
    return "".join(secrets.choice(ALPHABET) for _ in range(length))


def create_short_url(original_url, code_generator=generate_code):
    code = code_generator()
    while ShortURL.objects.filter(short_code=code).exists():
        code = code_generator()
    return ShortURL.objects.create(original_url=original_url, short_code=code)