from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Zapros
from .serializers import ZaprosSerializer


class ZaprosViewSet(viewsets.ModelViewSet):
    serializer_class = ZaprosSerializer
    queryset = Zapros.objects.all()
# Create your views here.
