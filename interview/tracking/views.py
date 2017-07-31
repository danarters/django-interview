# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render 

from .models import *

def home(request):
	context = {
		'is_new_visitor': 'TODO: determine if a user is new or not',
		'num_visits': 'TODO: determine number of page views a user has'
	}
	return render(request, 'index.html', context)
	