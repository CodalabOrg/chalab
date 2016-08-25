# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 16:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0014_datasetmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasetmodel',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
