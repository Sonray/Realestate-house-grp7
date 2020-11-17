from .serializer import RevSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from .models import Review
# Create your views here.




class RevList(APIView):
    # permission_classes = (IsAdminOrReadOnly,)

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


#  def delete(self, request, pk, format=None):
#         Review = self.get_user(pk)
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)






























# class Review (APIView):
    
#     def get_user(self, pk):
#         try:
#             return  Review.objects.get(pk=pk)
#         except Review.DoesNotExist:
#             return Http404

#     permission_classes = (IsAdminOrReadOnly,)
        
#     def get(self,request, pk, format=None):
#         the_user = self.get_user(pk)
#         serializers =  ReviewSerializer(the_user)
#         return Response(serializers.data) 

#     def post(self, request, format=None):
#         serializers = ReviewSerializer(data=request.data)

#         if serializers.is_valid():

#             serializers.save()

#             return Response(serializers.data, status=status.HTTP_201_CREATED)

#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self, request, pk, format=None):
#         Review = self.get_user(pk)
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)