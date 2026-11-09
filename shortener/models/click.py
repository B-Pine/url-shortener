from django.db import models
from .shorturl import ShortURL


class Click(models.Model):
    url = models.ForeignKey(ShortURL, on_delete=models.CASCADE, related_name="clicks")
    clicked_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    user_agent = models.CharField(blank=True)
    referrers = models.URLField(blank=True, max_length=2048)

    def __str__(self):
        return f"Click on {self.url.short_code} at {self.clicked_at}"