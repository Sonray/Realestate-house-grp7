from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from django.utils import timezone
from django.core.mail import send_mail

class RegisterSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(max_length=280)
    email = serializers.EmailField(max_length=50)
    date_joined = serializers.DateTimeField(default=timezone.now)
    type = serializers.ChoiceField(choices = ['REALTOR', 'USER'])
    password = serializers.CharField( max_length=280, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'type', 'password','date_joined' ]
        
    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email',('email is already in use')})
        send_mail(
            'WELCOME TO HOME MARVENS',
            'Home Mavens is a site where home-seekers can conveniently search for homes at the click of a button. It offers a wide selection of homes for both buyers and renters in numerous locations all over Kenya. It also allows landlords and home-sellers to post their properties so that potential buyers or renters can view them and contact them.',
            'davidokwacha@gmail.com',
            [email,],
            fail_silently=False,
        )
        return super().validate(attrs)
    
    #change save to create
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def __str__(self):
        return User

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'token',]
        extra_kwargs = {
            'password':{'write_only':True}
        }
    def validate(self, data):
        return data

