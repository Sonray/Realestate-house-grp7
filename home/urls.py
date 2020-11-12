from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from django.urls import path, include
from .views import UserProfile
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('users/<user_id>/profile/', UserProfile,)


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)