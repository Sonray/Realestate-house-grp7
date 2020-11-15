from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsAdminOrReadOnly
from .models import User
from .serializer import RegisterSerializer, LoginSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib import auth
import jwt
from django.conf import settings

# Create your views here.
class User_Register(APIView):
        
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Http404

    def get(self,request, pk, format=None):
        the_user = self.get_user(pk)
        serializers = RegisterSerializer(the_user)
        return Response(serializers.data)

    def post(self, request, format=None):

        serializers = RegisterSerializer(data=request.data)

        if serializers.is_valid():

            serializers.save()

            return Response(
                serializers.data, status=status.HTTP_201_CREATED
                )

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        permission_classes = (IsAdminOrReadOnly,)
        merch = self.get_user(pk)
        serializers = RegisterSerializer(merch, request.data)
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



class User_Login(APIView):
    # def get_user(self, pk):
    #     try:
    #         return User.objects.get(pk=pk)
    #     except Post.DoesNotExist:
    #         return Http404

    # def get(self,request, pk, format=None):
    #     the_user = self.get_user(pk)
    #     return Response(serializers.data)

    # def post(self, request):
    #     data = request.data
    #     username = data.get('username', '')
    #     password = data.get('password', '')

    #     user = auth.authenticate(username=username, password=password, )

    #     if user:
    #         auth_token = jwt.encode({'username':user.username, 'password':user.password}, settings.JWT_SECRET_KEY,)

    #         serializer = LoginSerializer(user)

    #         data  = { 'user':serializer.data, 'token':auth_token }
    #         return Response( data, status=status.HTTP_200_OK )

    #     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = LoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response( data, status=status.HTTP_200_OK )
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)