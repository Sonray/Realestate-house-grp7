from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    url(r'/register/', views.User_Register.as_view()),
    url(r'^api/get_user/(?P<pk>[0-9]+)/$', views.User_Register.as_view()),
    url(r'^api/delete_user/(?P<pk>[0-9]+)/$', views.User_Register.as_view()),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)