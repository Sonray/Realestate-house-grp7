from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsAdminOrReadOnly
from .models import User
from .serializer import RegisterSerializer, LoginSerializer
from rest_framework import status

# Create your views here.
class User_request(APIView):
        
    def get_user(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Http404

    def get(self,request, pk, format=None):
        the_user = self.get_user(pk)
        serializers = ProductSerializer(the_user)
        return Response(serializers.data)

    def post(self, request, format=None):
        permission_classes = (IsAdminOrReadOnly,)
        serializers = ProductSerializer(data=request.data)

        if serializers.is_valid():

            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        permission_classes = (IsAdminOrReadOnly,)
        merch = self.get_user(pk)
        serializers = ProductSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        permission_classes = (IsAdminOrReadOnly,)
        merch = self.get_user(pk)
        merch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)