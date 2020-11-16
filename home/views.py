<<<<<<< HEAD
from django.shortcuts import render
from .serializers import HouseSerializer
from .models import House
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404


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

class HouseDetail(APIView):

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
        return Response(status=status.HTTP_204_NO_CONTENT)
=======
from . serializer import RevSerializer
from .models import Review
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.



class Review (APIView):

    permission_classes = (IsAdminOrReadOnly,)
    
    def get(self, request, format=None):
        all_post = Review.objects.all()
        serializers = ReviewSerializer(all_post, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ReviewSerializer(data=request.data)

        if serializers.is_valid():

            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        Review = self.get_user(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
>>>>>>> 08c33c54434eab40017cda985d4cb93c8b0357b5
