from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from .permissions import IsAdminOrReadOnly

# Create your views here.

