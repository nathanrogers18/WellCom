# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wellcom_app', '0008_auto_20160918_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
