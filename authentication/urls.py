from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    url(r'/theregister/', views.User_Register.as_view(), name='register'),
    url(r'^api/get_user/(?P<pk>[0-9]+)/$', views.User_Register.as_view(), name='get_user'),
    url(r'^api/update_user/(?P<pk>[0-9]+)/$', views.User_Register.as_view(), name='update_user'),
    path('api/change-password/', views.ChangePassword.as_view(), name='change-password'),
    path('api/verify_email/', views.User_Register.as_view(), name='verify_email'),
    url(r'^api/login/', views.User_Login.as_view(), name='login'),
    url(r'^api/logout/', views.User_logout.as_view(), name='logout'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)