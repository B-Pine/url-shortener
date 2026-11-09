from rest_framework.generics import CreateAPIView, ListCreateAPIView

from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
)

from shortener.models import ShortURL
from shortener.serializers.shorturl import ShortURLSerializer


@extend_schema_view(
    post=extend_schema(
        summary="Create a short URL",
        examples=[
            OpenApiExample(
                "Valid request",
                value={"original_url": "https://www.djangoproject.com/"},
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
    )
)
class ShortURLCreateView(CreateAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer