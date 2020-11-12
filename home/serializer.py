from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class ProfileSerializer
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        """Create and return a new user."""
        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )