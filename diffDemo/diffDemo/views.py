# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect

def home(request):
    """Return the last five published questions."""
    return HttpResponseRedirect('/diff/')
