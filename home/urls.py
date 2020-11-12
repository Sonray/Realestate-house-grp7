from django.urls import path, include
from django.conf.urls import url
#from django.contrib.auth import views as auth_views
from rest_framework import routers
from .views import InquiryViewSet
from . import views
#from django.conf import settings
#from django.conf.urls.static import static
#from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'inquiry', views.InquiryViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]