from django.db import models
from django.conf import settings

from .tag import Tag
from .managers import URLManager


class ShortURL(models.Model):
    original_url = models.URLField(max_length=2048)
    short_code = models.CharField(max_length=10, unique=True)
    custom_alias = models.CharField(max_length=30, null=True, unique=True, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="urls",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    favicon = models.URLField(max_length=2048, blank=True)
    click_count = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name="urls", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    objects = URLManager()

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"