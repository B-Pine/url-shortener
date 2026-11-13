from rest_framework.routers import DefaultRouter

from .views import ShortURLViewSet

router = DefaultRouter()
router.register("urls", ShortURLViewSet, basename="shorturl")

urlpatterns = router.urls
