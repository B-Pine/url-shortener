from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user model"""
    class Tier(models.TextChoices):
        FREE = "free", "Free"
        PREMIUM = "premium", "Premium"
        ADMIN = "admin", "Admin"

    email = models.EmailField(unique=True)
    tier = models.CharField(max_length=10, choices=Tier.choices, default=Tier.FREE)

    @property
    def is_premium(self):
        return self.tier in {self.Tier.PREMIUM, self.Tier.ADMIN}