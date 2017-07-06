# File: places/urls.py
# -*- coding: utf-8 -*-

import os, sys
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dist/', views.dist, name='dist'),
    url(r'^getHome/', views.getHome, name='getHome'),
    # minP, maxP: either 0 or integer 1 thru 999,999,999 -- with our without commas
    url(ur'^showHome/'
    ur'(?P<homeTown>[a-zA-Z0-9 áéíóúÁÉÍÓÚüÜñÑ-]+)/'
    ur'(?P<homeState>[a-zA-Z]{2})/'
    ur'(?P<dist>[1-9]\d?(\d|(,?\d{3}))?)/'
    ur'(?P<sorter>[1-5])/'
    ur'(?P<minP>0|([1-9]\d{,2}(((,\d{3}){,2})|((\d{3}){,2}))))/'
    ur'(?P<maxP>0|([1-9]\d{,2}(((,\d{3}){,2})|((\d{3}){,2}))))/', \
            views.showHome, name='showHome'),
    url(r'^(?P<state>\w{2})/(?P<town>[a-zA-Z ]+)/', views.popn, name='popn'),
]

# ,\s*[A-Za-z]{2})/'
