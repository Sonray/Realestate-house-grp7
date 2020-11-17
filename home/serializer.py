from rest_framework import serializers
from .models import Review
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import UserProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name',)
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        """Create and return a new user."""
        user = UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

class RevSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

