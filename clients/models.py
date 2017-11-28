# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Ticket Model
# Anonymous clients send tickets to byrd
class TicketModel(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    subject = models.CharField(max_length=100, blank=False)
    ticket_type = models.CharField(max_length=50, blank=False,
                               choices=[('Bug Report', 'Bug Report'),
                                        ('Feature Request', 'Feature Request'),
                                        ('Other', 'Other')])
    urgency = models.CharField(max_length=50, blank=False,
                                   choices=[('Low', 'Low'),
                                            ('Mid', 'Mid'),
                                            ('High', 'High')])
    message = models.TextField(max_length=9999)
    status = models.CharField(max_length=50, default="Open",
                                   choices=[('Open', 'Open'),
                                            ('In Progress', 'In Progress'),
                                            ('Completed', 'Completed'),
                                            ('Rejected', 'Rejected')])
