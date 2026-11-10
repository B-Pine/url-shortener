from datetime import timedelta
import secrets
import string

from django.db import transaction
from django.db.models import F, Count
from django.utils import timezone

from .models import ShortURL, Click

ALPHABET = string.ascii_letters + string.digits
CODE_LENGTH = 7


def generate_code(length=CODE_LENGTH):
    return "".join(secrets.choice(ALPHABET) for _ in range(length))


def create_short_url(original_url, code_generator=generate_code):
    code = code_generator()
    while ShortURL.objects.filter(short_code=code).exists():
        code = code_generator()
    return ShortURL.objects.create(original_url=original_url, short_code=code)


def record_click(url: ShortURL, ip_address, user_agent, referrers):
    with transaction.atomic():
        ShortURL.objects.filter(pk=url.pk).update(click_count=F("click_count") + 1)
        Click.objects.create(
            url=url,
            ip_address=ip_address or None,
            user_agent=user_agent,
            referrers=referrers[:2048]
        )
        

def get_url_analytics(url):
    week_ago = timezone.now() - timedelta(days=7)
    totals = url.clicks.aggregate(
        total=Count("id"),
        last_7_days=Count("id", filter=Q(clicked_at__gte=week_ago)),
    )
    by_country = url.clicks.values("country").annotate(clicks=Count("id")).order_by("-clicks")
    return {**totals, "by_country": list(by_country)}