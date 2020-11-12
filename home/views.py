from rest_framework import viewsets
from .models import Inquiry
from .serializers import InquirySerializer


# Create your views here.

class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer