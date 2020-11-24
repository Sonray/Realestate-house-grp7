from rest_framework import serializers
from .models import House, Review

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model=House
        fields = ('id','image','name','description','price','category','location','date_added','user','bath','bed',)


class RevSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

