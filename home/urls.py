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
<<<<<<< HEAD
=======
    path(r'^viewset/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'^api/review/$', views.RevList.as_view()),      

    path('api/profile/', views.UserProfileList.as_view()),

    # path(r'^review/(?P<user_id>\d+)', views.Review.as_view()),
    # url(r'^api/get-review/(?P<pk>[0-9]+)/', views.review.as_view()),
    # url(r'^review/(?P<user_id>\d+)', views.Review.as_view()),
    # url(r'^api/review/(?P<pk>[0-9]+)/', views.Review.as_view()),
    path('api/review/', views.RevList.as_view()),
       
    path('api/houses/', views.HouseList.as_view()),
    path('api/house/<int:pk>', views.HouseDetail.as_view()),
    # url(r'^review/(?P<user_id>\d+)', views.Review.as_view()),
    # url(r'^api/get-review/(?P<pk>[0-9]+)/', views.Review.as_view()),
>>>>>>> main
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
