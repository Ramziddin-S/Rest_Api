from rest_framework import serializers
from .models import Zavod, Vloyat, Mashena


class VloyatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vloyat
        fields = "__all__"


class ZavodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Zavod
        fields = "__all__"


class MashenaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mashena
        fields = "__all__"
