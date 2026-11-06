from django.urls import path

from .views import ShortURLCreateView

urlpatterns = [
    path("urls/", ShortURLCreateView.as_view(), name="url-create"),
]