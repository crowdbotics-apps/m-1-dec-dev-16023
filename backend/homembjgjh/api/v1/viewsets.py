from rest_framework import authentication
from homembjgjh.models import Hfgjhgfk
from .serializers import HfgjhgfkSerializer
from rest_framework import viewsets


class HfgjhgfkViewSet(viewsets.ModelViewSet):
    serializer_class = HfgjhgfkSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Hfgjhgfk.objects.all()
