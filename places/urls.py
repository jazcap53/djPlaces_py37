# File: places/urls.py
# -*- coding: utf-8 -*-

import os, sys
from django.conf.urls import url

from . import views

app_name = 'places'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getHome/', views.getHome, name='getHome'),
    # minP, maxP: non-negative integer thru 999,999,999 -- commas optional
    url(r'^showHome/'
        r'(?P<homeTown>[a-zA-Z0-9 áéíóúÁÉÍÓÚüÜñÑ-]+)/'
        r'(?P<homeState>[a-zA-Z]{2})/'
        r'(?P<dist>[1-9]\d?(\d|(,?\d{3}))?)/'
        r'(?P<sorter>[1-5])/'
        r'(?P<minP>0|([1-9]\d{,2}(((,\d{3}){,2})|((\d{3}){,2}))))/'
        r'(?P<maxP>0|([1-9]\d{,2}(((,\d{3}){,2})|((\d{3}){,2}))))/', \
            views.showHome, name='showHome'),
]
