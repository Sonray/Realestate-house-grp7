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
from django.contrib import admin
<<<<<<< HEAD
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
=======
>>>>>>> main

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'',include('home.urls')),
    url(r'',include('authentication.urls')),
<<<<<<< HEAD
    url(r'api/token/', TokenObtainPairView.as_view()),
    url(r'api/token/refresh/', TokenRefreshView.as_view()),

]
=======
]
>>>>>>> main
