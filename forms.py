from django import forms
from django.conf import settings
from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext as _
from djangosingkat.models import Pranala

class NewPranala(forms.ModelForm):
    class Meta:
        model = Pranala
        exclude = ( 'date_created' )
