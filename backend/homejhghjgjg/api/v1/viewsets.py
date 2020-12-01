from rest_framework import authentication
from homejhghjgjg.models import Hgfdjhfjgh
from .serializers import HgfdjhfjghSerializer
from rest_framework import viewsets


class HgfdjhfjghViewSet(viewsets.ModelViewSet):
    serializer_class = HgfdjhfjghSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Hgfdjhfjgh.objects.all()
