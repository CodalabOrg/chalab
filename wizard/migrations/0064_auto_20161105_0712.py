# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-05 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0063_auto_20161029_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='protocolmodel',
            name='dev_execution_time_limit',
            field=models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Development phase execution time limit (seconds)'),
        ),
        migrations.AddField(
            model_name='protocolmodel',
            name='dev_phase_description',
            field=models.CharField(default='Development Phase', max_length=256),
        ),
        migrations.AddField(
            model_name='protocolmodel',
            name='final_execution_time_limit',
            field=models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Final phase execution time limit (seconds)'),
        ),
        migrations.AddField(
            model_name='protocolmodel',
            name='final_phase_description',
            field=models.CharField(default='Final Phase', max_length=256),
        ),
    ]
