from django.shortcuts import render
from .serializers import HouseSerializer
from .models import House
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class HouseList(APIView):

    def get(self, request, format=None):
        all_houses = House.objects.all()
        serializers=HouseSerializer(all_houses, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = HouseSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)