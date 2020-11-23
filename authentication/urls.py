from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    url(r'/theregister/', views.User_Register.as_view(), name='register'),
    url(r'^api/get_user/(?P<pk>[0-9]+)/$', views.User_Register.as_view(), name='get_user'),
    url(r'^api/update_user/(?P<pk>[0-9]+)/$', views.User_Register.as_view(), name='update_user'),
    url(r'^api/login/', views.User_Login.as_view(), name='login'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)