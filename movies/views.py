# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .api import *

# Create your views here.
def movies(request):
    movie_name = str(request.POST.get('movie'))
    locations = get_movie_locations(movie_name)
    return render(request, 'map.html', {'locations': locations})