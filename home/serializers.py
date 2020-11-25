from rest_framework import serializers
from .models import Inquiry
from authentication.models import User

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ['id', 'name', 'message', 'user', 'location', 'contact']