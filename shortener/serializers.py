from rest_framework import serializers

from .models import ShortURL
from .services import create_short_url


class ShortURLSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = ShortURL
        fields = ["original_url", "short_code", "short_url", "created_at"]
        read_only_fields = ["short_code", "created_at"]

    def get_short_url(self, obj):
        return self.context["request"].build_absolute_uri(f"/{obj.short_code}/")

    def create(self, validated_data):
        return create_short_url(validated_data["original_url"])