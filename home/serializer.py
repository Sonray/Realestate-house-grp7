from rest_framework import serializers
from .models import Review
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class RevSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

from .models import House

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model=House
        fields = ('id','image','description','price','category','location','date_added','user',)
