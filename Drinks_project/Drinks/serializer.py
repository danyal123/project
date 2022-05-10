import imp
from re import M
from rest_framework import serializers
from .Models import Drinks


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = ['id','name','description']
