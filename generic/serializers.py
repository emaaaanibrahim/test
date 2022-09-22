from rest_framework import serializers
from . models import GenericModel


class GenericSerializer (serializers.ModelSerializer):
    class Meta:
        model=GenericModel
        fields="__all__"