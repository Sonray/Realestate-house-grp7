from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
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
