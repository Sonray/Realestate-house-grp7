"""marven URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from rest_framework.authtoken.views import obtain_auth_token

from django.contrib import admin
from django.urls import path, include
#from django.conf import settings
#from django.conf.urls.static import static



urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'',include('home.urls')),
    url(r'',include('authentication.urls')),
    url(r'api/token/', TokenObtainPairView.as_view()),
    url(r'api/token/refresh/', TokenRefreshView.as_view()),
]