#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from clients.models import *


class TicketForm(forms.ModelForm):

    class Meta:
        model = TicketModel
        fields = '__all__'
