# -*- coding: utf-8 -*-
# comment
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

LOGIN_URL = settings.LOGIN_URL


class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, request, *args, **kwargs):
        return super(
            LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
