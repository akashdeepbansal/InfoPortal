from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class user_details(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    font = models.IntegerField(default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)])
    mode = (
        (u'1', u'Daymode'),
        (u'2', u'Nightmode'),
    )
    mode = models.CharField(default = 1 ,max_length=1, choices=mode)
    def __str__(self):
        return self.email
