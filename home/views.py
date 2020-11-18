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
