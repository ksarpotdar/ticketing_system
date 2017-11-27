# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import *
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from ticketing_system.views_mixins import LoginRequiredMixin
from support.forms import LoginForm
from clients.models import TicketModel


# IT Support login view
class SupportLoginView(TemplateView):
    template_name = "support/login.html"

    def get_context_data(self, **kwargs):
        context = super(
            SupportLoginView, self).get_context_data(**kwargs)

        context['form'] = LoginForm

        return context

    def post(self, request, *args, **kwargs):
        # Receive POST from form in template
        form = LoginForm(request.POST)
        # If form is valid, check if authenticated
        if form.is_valid():
            # Uses the authenticate django method to authenticate user
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            # If user is authenticated, uses login django method
            if user:
                login(request, user)
                form = LoginForm
                messages.success(request, 'Successfully authenticated!')
                return HttpResponseRedirect(reverse_lazy('tickets'))
            # If user is not authenticated, error message
            else:
                form = LoginForm
                messages.success(request, 'There was an error authenticating')
                return render(request, self.template_name, {'success': False,
                                                            'form': form})
        # If form invalid, error message
        else:
            form = LoginForm
            messages.success(request, 'There was an error authenticating')
            return render(request, self.template_name, {'success': False,
                                                        'form': form})
            return HttpResponseRedirect(reverse_lazy('support_login'))


class TicketsView(LoginRequiredMixin, ListView):
    template_name = 'support/tickets.html'
    model = TicketModel
    context_object_name = 'tickets'
