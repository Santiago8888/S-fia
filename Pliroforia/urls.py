# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:07:45 2016

@author: dAVID
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.busqueda, name='búsqueda'),
]