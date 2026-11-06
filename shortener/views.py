from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET
from rest_framework import generics

from .models import ShortURL
from .serializers import ShortURLSerializer


class ShortURLCreateView(generics.CreateAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer


@require_GET
def redirect_view(request, short_code):
    url = get_object_or_404(ShortURL, short_code=short_code)
    return HttpResponseRedirect(url.original_url)