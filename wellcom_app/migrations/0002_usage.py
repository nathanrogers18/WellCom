# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 23:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wellcom_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('usage_count', models.IntegerField()),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wellcom_app.Well')),
            ],
        ),
    ]
