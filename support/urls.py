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
    url(
        r'^logout/$',
                logout,
        {
            'next_page': '/'
        },
        name='logout'),
    url(
        r'^edit-ticket/(?P<id>\d+)/$',
        EditTicketView.as_view(),
        name='edit_ticket'),
    url(
        r'^delete-ticket/(?P<id>\d+)/$',
        delete_ticket,
        name='delete_ticket'),
]
