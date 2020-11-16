from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/houses/', views.HouseList.as_view()),
    url(r'api/house/house-id/(?P<pk>[0-9]+)/$',views.HouseDetail.as_view()),
    url(r'^review/(?P<user_id>\d+)', views.Review.as_view()),
    url(r'^api/get-review/(?P<pk>[0-9]+)/', views.Review.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)