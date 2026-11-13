from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from shortener.models import ShortURL
from shortener.services import record_click


@api_view(["GET"])
def redirect_view(request, short_code):
    url = get_object_or_404(ShortURL.objects.active_urls(), short_code=short_code)
    record_click(
        url=url,
        ip_address=request.META.get("REMOTE_ADDR"),
        user_agent=request.META.get("HTTP_USER_AGENT", ""),
        referrer=request.META.get("HTTP_REFERER", ""),
    )
    return HttpResponseRedirect(url.original_url)
