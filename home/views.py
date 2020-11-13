from .serializer import ProfileSerializer
from .models import UserProfile
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

# Profile views
class UserProfileList(APIView):
     def get(self, request, format=None):
        all_profile = UserProfile.objects.all()
        serializers=ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)