# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from test import save_author


def index(request):
    save_author()
    return HttpResponse("Hello, world. You're at the mysqlpool index.")
