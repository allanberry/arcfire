# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-07 06:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcfire', '0006_auto_20151107_0633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thing',
            name='heading',
        ),
    ]
