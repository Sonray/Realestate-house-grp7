from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from .views import InquiryViewSet
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register(r'inquiry', views.InquiryViewSet)
urlpatterns = [
    path(r'^viewset/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'^api/review/$', views.RevList.as_view()),      
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
