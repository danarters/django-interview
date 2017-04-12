# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

def home(request):
	is_new_visitor = 'TODO: determine if a user is new or not'
	if is_new_visitor:
		return HttpResponse('Hello new customer!')
	else:
		return HttpResponse('Hello returning customer!')