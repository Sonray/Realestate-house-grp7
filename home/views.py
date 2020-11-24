from rest_framework import viewsets,status
from .models import Inquiry
from .serializers import InquirySerializer
from .serializer import RevSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsAdminOrReadOnly
from .models import Review

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
