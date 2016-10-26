# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:59:22 2016

@author: dAVID
"""

from django.contrib.auth.forms import AuthenticationForm 
from django import forms

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))