from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from shortener.models import ShortURL


@api_view(["GET"])
def redirect_view(request, short_code):
    url = get_object_or_404(ShortURL, short_code=short_code)
    return HttpResponseRedirect(url.original_url)