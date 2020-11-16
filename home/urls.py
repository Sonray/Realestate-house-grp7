from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

        url(r'^review/(?P<user_id>\d+)', views.review, name='review'),
        url(r'^api/get-review/(?P<pk>[0-9]+)/', views.review.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)