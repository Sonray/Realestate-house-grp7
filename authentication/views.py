from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsAdminOrReadOnly
from .models import User
from .serializer import RegisterSerializer, LoginSerializer
from rest_framework import status
from django.contrib import auth
import jwt
from django.conf import settings

# Create your views here.
class User_Register(APIView):
    pass
    # def get_user(self, pk):
    #     try:
    #         return User.objects.get(pk=pk)
    #     except Post.DoesNotExist:
    #         return Http404

    # def get(self,request, pk, format=None):
    #     the_user = self.get_user(pk)
    #     serializers = RegisterSerializer(the_user)
    #     return Response(serializers.data)

    def post(self, request):
        serializers = RegisterSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(
                serializers.data, status=status.HTTP_201_CREATED
                )
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, *args, **kwargs):
    #     pass
    #     data = request.data
    #     serializer = LoginSerializer(data=data)

    #     if serializer.is_valid(raise_exception=True):
    #         new_data = serializer.data
    #         return Response( new_data, status=status.HTTP_200_OK )
    #     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # user = serializer.save()
        # return Response({
        #     'user': RegisterSerializer(user, context = self.get_serializer_context()).data,
        #     "token": AccessToken.objects.create(user)[1]
        # })

    
    # def put(self, request, pk, format=None):        
    #     merch = self.get_user(pk)
    #     serializers = RegisterSerializer(merch, request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data)
    #     else:
    #         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):        
    #     merch = self.get_user(pk)
    #     merch.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class User_Login(APIView):
    pass

    # def post(self, request, *args, **kwargs):
    #     data = request.data
    #     serializer = LoginSerializer(data=data)

    #     if serializer.is_valid(raise_exception=True):
    #         new_data = serializer.data
    #         return Response( data, status=status.HTTP_200_OK )
    #     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
