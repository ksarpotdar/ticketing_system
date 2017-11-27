from django.conf.urls import url
from support.views import *
from django.contrib.auth.views import *


urlpatterns = [
    url(
        r'^support_login$',
        SupportLoginView.as_view(),
        name='support_login'),
    url(
        r'^tickets$',
        TicketsView.as_view(),
        name='tickets'),
]
