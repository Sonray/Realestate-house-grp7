from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from rest_framework import routers
from .views import InquiryViewSet, UserProfileList
from . import views
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'inquiry', views.InquiryViewSet)
urlpatterns = [

    url(r'^review/(?P<user_id>\d+)', views.Review.as_view(), name='review'),
    url(r'^api/get-review/(?P<pk>[0-9]+)/', views.Review.as_view()),
    url(r'^api/houses/', views.HouseList.as_view()),
    url(r'^api/house/house-id/(?P<pk>[0-9]+)/$',views.HouseDetail.as_view()),
    url(r'', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/profile/', views.UserProfileList.as_view()),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

