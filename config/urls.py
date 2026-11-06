from django.contrib import admin
from django.urls import include, path

from shortener.views import redirect_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("shortener.urls")),
    path("<str:short_code>/", redirect_view, name="redirect"),
]