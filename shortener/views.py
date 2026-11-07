from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.decorators import api_view

from .models import ShortURL
from .serializers import ShortURLSerializer

from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
)


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


@api_view(["GET"])
def redirect_view(request, short_code):
    url = get_object_or_404(ShortURL, short_code=short_code)
    return HttpResponseRedirect(url.original_url)