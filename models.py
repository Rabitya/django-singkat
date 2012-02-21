from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _

import datetime

class Pranala(models.Model):
    alias = models.CharField(_('alias'), max_length=255, null=False, unique=True)
    pranala = models.URLField(_('pranala'), max_length=255, null=False)
    date_created = models.DateTimeField(_('date created'), default=datetime.datetime.today())
    def __unicode__(self):
        return self.alias