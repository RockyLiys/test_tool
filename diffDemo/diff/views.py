# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import RequestContext
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def index(request):
    context = RequestContext(request)
    print context
    template = loader.get_template('index.html')
    print request
    return HttpResponse(template.render({}, request))
