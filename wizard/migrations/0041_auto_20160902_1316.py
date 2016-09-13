# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0040_challengemodel_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challengemodel',
            name='dataset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wizard.DatasetModel'),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='documentation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='challenge', to='wizard.DocumentationModel'),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='metric',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wizard.MetricModel'),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='protocol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='challenge', to='wizard.ProtocolModel'),
        ),
        migrations.AlterField(
            model_name='challengemodel',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wizard.TaskModel'),
        ),
    ]