from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from django.utils import timezone

class RegisterSerializer(serializers.Serializer):
    
    username = serializers.CharField(max_length=280)
    email = serializers.EmailField(max_length=50)
    date_joined = serializers.DateTimeField(default=timezone.now)
    type = serializers.ChoiceField(choices = ['Realtor', 'A_User'])
    password = serializers.CharField( max_length=280)

    def __str__(self):
        return f'username'

    class Meta:
        model = User
        fields = ['username', 'email', 'type', 'password' ]
        extra_kwargs = {
            'password':{'write_only':True}
        }
    
    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email',('email is already in use')})
        return super().validate(attrs)
    
    #change save to create
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password',)
        extra_kwargs = {
            'password':{'write_only':True}
        }