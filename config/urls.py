from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from shortener.views import redirect_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("shortener.urls")),
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
     path("api/v1/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("<str:short_code>/", redirect_view, name="redirect"),
]