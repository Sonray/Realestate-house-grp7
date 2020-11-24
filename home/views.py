from rest_framework import viewsets,status
from .models import Inquiry
from .serializers import InquirySerializer
from .serializer import RevSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from .permissions import IsAdminOrReadOnly
from .models import Review
from .serializer import ProfileSerializer, RevSerializer
from .models import UserProfile, Review 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404,HttpResponse
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from .serializer import RevSerializer
from django.shortcuts import render
from .serializer import HouseSerializer,RevSerializer
from .models import House,Review
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,permissions
from django.http import Http404
from .permissions import IsAdminOrReadOnly,IsOwnerOrReadOnly

# Profile views
class UserProfileList(APIView):
     def get(self, request, format=None):
        all_profile = UserProfile.objects.all()
        serializers=ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

     def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(
                serializers.data, status=status.HTTP_201_CREATED
                )
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class HouseList(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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

class HouseDetail(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self,pk):
        '''
        retrieve house object from database
        '''

        try:
            return House.objects.get(pk=pk)
        except House.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        '''
        get a single house object with its details
        '''

        house=self.get_object(pk)
        serializer=HouseSerializer(house)
        return Response(serializer.data) 

    def put(self, request, pk, format=None):
        '''
        update details of a single house object
        '''

        house=self.get_object(pk)
        serializer = HouseSerializer(house, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        house = self.get_object(pk)
        house.delete()

class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

    def get(self, request, format=None):
        inquiry = Inquiry.objects.all()
        serializer = InquirySerializer(inquiry, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = InquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk=None):
        pk = self.kwargs.get('pk')
        inquiry = Inquiry.objects.filter(pk = pk)
        Inquiry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self, request, format=None):
        serializer = InquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RevList(APIView):

    def get(self, request, format=None):
        all_merchrev = Review.objects.all()
        serializers = RevSerializer(all_merchrev, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers =RevSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)