from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
)
from rest_framework.generics import ListCreateAPIView

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
)
class ShortURLListCreateView(ListCreateAPIView):
    queryset = ShortURL.objects.prefetch_related("tags")
    serializer_class = ShortURLSerializer
    filter_backends = [DjangoFilterBackend, StableOrderingFilter]
    filterset_class = ShortURLFilter
    ordering_fields = ["created_at", "click_count"]
    ordering = ["-created_at"]
