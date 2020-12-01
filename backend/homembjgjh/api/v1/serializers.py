from rest_framework import serializers
from homembjgjh.models import Hfgjhgfk


class HfgjhgfkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hfgjhgfk
        fields = "__all__"
