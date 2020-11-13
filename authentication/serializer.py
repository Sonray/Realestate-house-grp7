from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator

class RegisterSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'type', 'password' )
        extra_kwargs = {
            'password':{'write_only':True}
        }
    
    def save(self, validated_data):
        user = User.objects.create(validated_data['username'], validated_data['email'], 
            validated_data['type'], validated_data['password'])
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