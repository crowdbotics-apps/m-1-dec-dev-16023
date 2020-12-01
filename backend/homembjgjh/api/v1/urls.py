from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import HfgjhgfkViewSet

router = DefaultRouter()
router.register("hfgjhgfk", HfgjhgfkViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
