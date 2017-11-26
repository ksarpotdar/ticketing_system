# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import CreateView
from clients.models import TicketModel
from clients.forms import TicketForm


# Initial view. Anonymous users can fill the form and send tickets
# Byrd employees can choose register or login
class IndexView(CreateView):
    form_class = TicketForm
    template_name = 'index.html'
