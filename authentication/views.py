from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .permissions import IsAdminOrReadOnly
from .models import User
from .serializer import RegisterSerializer, LoginSerializer, ChangePasswordSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib import auth
import jwt
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from .util import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

# Create your views here.

@permission_classes((permissions.AllowAny,))
class User_Register(APIView ):

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

            # user_data = serializers.data
            # user = User.objects.get(email=user_data['email'])

            # token = RefreshToken.for_user(user).access_token

            # current_site = get_current_site(request)

            # relative_link = reverse('verify_email')

            # absUrl = "http://"+current_site+relative_link+"?token="+str(token)
            # data = {'domain': absUrl, 'to_email':user.email, 'subject':'verify your email'}
            # email_body = 'Hi '+user.username+' Use this link to verify your email'+absUrl

            # Util.send_email(data)


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

class Verify_email(APIView):
    def get(self):
        pass


class User_Login(APIView):
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = LoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response( data, status=status.HTTP_200_OK )
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class User_logout(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ChangePassword(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
