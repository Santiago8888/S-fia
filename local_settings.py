# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 09:56:20 2016

@author: dAVID
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True