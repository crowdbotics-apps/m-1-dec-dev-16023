from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import HgfdjhfjghViewSet

router = DefaultRouter()
router.register("hgfdjhfjgh", HgfdjhfjghViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
