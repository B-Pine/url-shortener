from django.db import models
from django.db.models import Q
from django.utils import timezone


class ShortURLQuerySet(models.QuerySet):
    def active_urls(self):
        now = timezone.now()
        return self.filter(Q(expires_at__isnull=True) | Q(expires_at__gt=now), is_active=True)

    def expired_urls(self):
        return self.filter(expires_at__lte=timezone.now())

    def popular_urls(self):
        return self.order_by("-click_count", "-created_at")