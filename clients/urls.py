from django.conf.urls import url
from clients.views import *
from django.contrib.auth.views import *


urlpatterns = [
    url(r'^$',
        IndexView.as_view(),
        name='index'),
]
