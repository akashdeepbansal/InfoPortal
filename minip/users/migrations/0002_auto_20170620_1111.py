# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-20 11:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_details',
            old_name='Password',
            new_name='password',
        ),
    ]
