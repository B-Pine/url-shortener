from django.contrib import admin

from .models import ShortURL, Click, Tag

@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ("short_code", "original_url", "owner", "is_active", "click_count", "created_at")
    list_filter = ("is_active",)
    search_fields = ("short_code", "original_url")
    list_select_related = ("owner",)

    def get_queryset(self, request):
        return super().get_queryset(request).with_relations()

    @admin.display(description="Tags")
    def tag_list(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())
    

@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ("url", "clicked_at", "country", "ip_address")


admin.site.register(Tag)