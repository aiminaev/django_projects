from rest_framework import serializers
from .models import Zapros


class ZaprosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zapros
        fields = ('search_text',)
