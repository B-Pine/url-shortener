from django.urls import path

from .views import ShortURLListCreateView

urlpatterns = [
    path("urls/", ShortURLListCreateView.as_view(), name="url-list"),
]
