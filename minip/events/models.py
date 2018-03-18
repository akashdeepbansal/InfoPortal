from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class event_details(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    date = models.DateField(null=True)
    link = models.CharField(max_length=200 , null=True , blank=True)
    status = (
        (u'1', u'Approved'),
        (u'2', u'Not-Approved'),
    )
    status = models.CharField(default = 1 ,max_length=1, choices=status)

    def __str__(self):
        return self.title

class news_details(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=300)
    link = models.CharField(max_length=200 , null=True)
    status = (
        (u'1', u'Approved'),
        (u'2', u'Not-Approved'),
    )
    status = models.CharField(default = 1 ,max_length=1, choices=status)
    def __str__(self):
        return self.title
