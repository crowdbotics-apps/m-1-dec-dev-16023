from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import HgfjhfkjhgfkhViewSet

router = DefaultRouter()
router.register("hgfjhfkjhgfkh", HgfjhfkjhgfkhViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
