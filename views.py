from django import forms
from django.conf import settings
from django.core.context_processors import csrf
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import Context, loader, RequestContext
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_protect 
from djangosingkat.forms import NewPranala
from djangosingkat.models import Pranala
from random import choice

import string

def index(request):
    return HttpResponseRedirect("/createnew/")
    
def createnew(request):
    c = {}
    c.update(csrf(request))
    if request.method == "POST":
        form = NewPranala(request.POST)
        if form.is_valid():
            alias = form.cleaned_data.get('alias')
            if not set(alias).issubset("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
                return HttpResponseRedirect("/createnew/")
            form.save()
            data = { 'alias': alias, 'app_url': settings.APP_URL }
            return render_to_response('done.html', data, context_instance=RequestContext(request))
    else:
        form = NewPranala()
    newalias = ""
    chars = string.letters + string.digits
    for i in range(6):
        newalias = newalias + choice(chars)
    data = { 'form': form, 'app_url': settings.APP_URL, 'newalias':  newalias }
    return render_to_response('createnew.html', data, context_instance=RequestContext(request))

def goto(request, alias):
    result = get_object_or_404(Pranala, alias=alias)
    return HttpResponseRedirect("%s" % result.pranala)
    #data = { 'result': result, 'app_url': settings.APP_URL }
    #return render_to_response('goto.html', data, context_instance=RequestContext(request))
