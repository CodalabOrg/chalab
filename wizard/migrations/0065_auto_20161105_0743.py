# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-05 07:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0064_auto_20161105_0712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protocolmodel',
            name='allow_reuse',
        ),
        migrations.RemoveField(
            model_name='protocolmodel',
            name='has_registration',
        ),
        migrations.RemoveField(
            model_name='protocolmodel',
            name='publicly_available',
        ),
        migrations.RemoveField(
            model_name='protocolmodel',
            name='ranked_submissions',
        ),
    ]
