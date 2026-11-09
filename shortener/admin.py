from django.contrib import admin

from .models import ShortURL, Click, Tag

@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ("short_code", "original_url", "owner", "is_active", "click_count", "created_at")
    list_filter = ("is_active",)
    search_fields = ("short_code", "original_url")

@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ("url", "clicked_at", "country", "ip_address")


admin.site.register(Tag)