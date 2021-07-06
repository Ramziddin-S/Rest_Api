from rest_framework import viewsets
from .serializers import VloyatSerializers, ZavodSerializers, MashenaSerializers
from .models import Vloyat, Zavod, Mashena


class VloyatViewSet(viewsets.ModelViewSet):
    queryset = Vloyat.objects.all()
    serializer_class = VloyatSerializers


class ZavodViewSet(viewsets.ModelViewSet):
    queryset = Zavod.objects.all()
    serializer_class = ZavodSerializers


class MashenaViewSet(viewsets.ModelViewSet):
    queryset = Mashena.objects.all()
    serializer_class = MashenaSerializers
