from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import url
#from django.contrib.auth import views as auth_views
from rest_framework import routers
from .views import InquiryViewSet
from . import views
from django.urls import path, include
from .views import UserProfileList
from rest_framework.authtoken.views import obtain_auth_token
#from django.conf import settings
#from django.conf.urls.static import static
#from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'inquiry', views.InquiryViewSet)
urlpatterns = [

    url(r'^review/(?P<user_id>\d+)', views.review, name='review'),
    url(r'^api/get-review/(?P<pk>[0-9]+)/', views.review.as_view()),
    path('api/houses/', views.HouseList.as_view()),
    url(r'api/house/house-id/(?P<pk>[0-9]+)/$',views.HouseDetail.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('api/profile/', views.UserProfileList.as_view()),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

