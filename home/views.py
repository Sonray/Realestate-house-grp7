from .serializer import ProfileSerializer, RevSerializer
from .models import UserProfile, Review 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404,HttpResponse
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Profile views
class UserProfileList(APIView):
     def get(self, request, format=None):
        all_profile = UserProfile.objects.all()
        serializers=ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)



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
