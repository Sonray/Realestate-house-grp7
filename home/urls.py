from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from django.urls import path, include
from .views import UserProfileList
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('api/profile/', views.UserProfileList.as_view()),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)