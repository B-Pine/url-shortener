from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
)
from rest_framework import viewsets

from shortener.filters import ShortURLFilter, StableOrderingFilter
from shortener.models import ShortURL
from shortener.serializers.shorturl import ShortURLSerializer


@extend_schema_view(
    get=extend_schema(summary="List Short URLs (paginated, filterable,sortable)"),
    post=extend_schema(
        summary="Create a short URL",
        examples=[
            OpenApiExample(
                "Valid request",
                value={"original_url": "https://www.bugingo-innocent.me/"},
                request_only=True,
            ),
        ],
        responses={
            201: ShortURLSerializer,
            400: OpenApiResponse(
                description="Invalid input",
                examples=[
                    OpenApiExample(
                        "Invalid URL",
                        value={
                            "status_code": 400,
                            "message": "Validation failed.",
                            "errors": {"original_url": ["Enter a valid URL."]},
                        },
                    ),
                ],
            ),
        },
    ),
    retrieve=extend_schema(summary="Retrieve one of your short URLs"),
    update=extend_schema(summary="Update one of your short URLs"),
    partial_update=extend_schema(summary="Partially update one of your short URLs"),
    destroy=extend_schema(summary="Delete one of your short URLs"),
)
class ShortURLViewSet(viewsets.ModelViewSet):
    serializer_class = ShortURLSerializer
    lookup_field = "short_code"
    filter_backends = [DjangoFilterBackend, StableOrderingFilter]
    filterset_class = ShortURLFilter
    ordering_fields = ["created_at", "click_count"]
    ordering = ["-created_at"]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return ShortURL.objects.none()
        return ShortURL.objects.filter(owner=self.request.user).prefetch_related("tags")
