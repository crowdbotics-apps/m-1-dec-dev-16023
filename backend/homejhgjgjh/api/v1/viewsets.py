from rest_framework import authentication
from homejhgjgjh.models import Hgfjhfkjhgfkh
from .serializers import HgfjhfkjhgfkhSerializer
from rest_framework import viewsets


class HgfjhfkjhgfkhViewSet(viewsets.ModelViewSet):
    serializer_class = HgfjhfkjhgfkhSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Hgfjhfkjhgfkh.objects.all()
