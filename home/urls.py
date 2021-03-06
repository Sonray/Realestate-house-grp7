from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from .views import InquiryViewSet
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, include
from .views import UserProfileList
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'inquiry', views.InquiryViewSet)
urlpatterns = [
    url(r'^viewset/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/review/$', views.RevList.as_view()),
    path('api/profile/', views.UserProfileList.as_view()),
    path('api/review/', views.RevList.as_view()),       
    path('api/houses/', views.HouseList.as_view()),
    path('api/house/<int:pk>', views.HouseDetail.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
