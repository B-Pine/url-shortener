from rest_framework import serializers

from shortener.models import ShortURL, Tag

from ..services import create_short_url


class ShortURLSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()
    tags: "serializers.SlugRelatedField[Tag]" = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )

    class Meta:
        model = ShortURL
        fields = ["original_url", "short_code", "short_url", "tags", "click_count", "created_at"]
        read_only_fields = ["short_code", "click_count", "created_at"]

    def get_short_url(self, obj):
        return self.context["request"].build_absolute_uri(f"/{obj.short_code}/")

    def create(self, validated_data):
        return create_short_url(validated_data["original_url"])
