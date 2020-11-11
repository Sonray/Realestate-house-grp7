from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidatorfrom rest_framework import serializers
from .models import Review

class RevSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

