# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from clients.forms import TicketForm


# Initial view. Anonymous users can fill the form and send tickets
# Byrd employees can choose register or login
class IndexView(CreateView):
    form_class = TicketForm
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        # Receive POST from form in template
        form = TicketForm(request.POST)
        # If form is valid, save ticket submitted
        if form.is_valid():
            form.save()
            form = TicketForm
            messages.success(request, 'Your ticket was sent!')
            return render(request, self.template_name, {'success': True,
                                                        'form': form})
        # If form invalid, error message
        else:
            form = TicketForm
            messages.success(request, 'There was an error')
            return render(request, self.template_name, {'success': False,
                                                        'form': form})
            return HttpResponseRedirect(reverse_lazy('index'))
