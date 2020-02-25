from datetime import datetime

from django.db import models
from django.conf import settings

SHORTCODE_MAX =  getattr(settings,"SHORTCODE_MAX",15)

class Shorturl(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=SHORTCODE_MAX,blank=True,unique= True)
    timestamp = models.DateTimeField(default=datetime.now)
    active = models.BooleanField(default=True)

    def __str__(self):
        return  self.url