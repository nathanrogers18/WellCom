# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 19:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('temperature_c', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaterTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('pH', models.DecimalField(decimal_places=4, max_digits=15)),
                ('turbidity_ntu', models.DecimalField(decimal_places=4, max_digits=15)),
                ('app_true_colour_hz', models.IntegerField()),
                ('conductivity_uscm', models.DecimalField(decimal_places=4, max_digits=15)),
                ('temperature_c', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total_iron', models.DecimalField(decimal_places=4, max_digits=15)),
                ('calcium', models.DecimalField(decimal_places=4, max_digits=15)),
                ('magnesium', models.DecimalField(decimal_places=4, max_digits=15)),
                ('chloride', models.DecimalField(decimal_places=4, max_digits=15)),
                ('sulphate', models.DecimalField(decimal_places=4, max_digits=15)),
                ('suspended_solids', models.DecimalField(decimal_places=4, max_digits=15)),
                ('total_dissolved_solids', models.DecimalField(decimal_places=4, max_digits=15)),
                ('total_solids', models.DecimalField(decimal_places=4, max_digits=15)),
                ('total_alkalinity', models.DecimalField(decimal_places=4, max_digits=15)),
                ('total_hardness', models.DecimalField(decimal_places=4, max_digits=15)),
                ('calcium_hardness', models.DecimalField(decimal_places=4, max_digits=15)),
                ('magnesium_hardness', models.DecimalField(decimal_places=4, max_digits=15)),
                ('copper', models.DecimalField(decimal_places=4, max_digits=15)),
                ('nitrite_nitrogen', models.DecimalField(decimal_places=4, max_digits=15)),
                ('nitrate_nitrogen', models.DecimalField(decimal_places=4, max_digits=15)),
                ('fluoride', models.DecimalField(decimal_places=4, max_digits=15)),
                ('mpn_index_tc_per_deciliter', models.DecimalField(decimal_places=4, max_digits=15)),
                ('ammonia_nitrogen', models.DecimalField(decimal_places=4, max_digits=15)),
                ('manganese', models.DecimalField(decimal_places=4, max_digits=15)),
                ('aluminum', models.DecimalField(decimal_places=4, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=11)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=11)),
                ('country', models.CharField(max_length=200)),
                ('date_installed', models.DateField()),
                ('last_update', models.DateTimeField()),
                ('estimated_users', models.IntegerField()),
                ('cost_usd', models.DecimalField(decimal_places=2, max_digits=8)),
                ('contractor', models.CharField(max_length=200)),
                ('flow_rate_lpm', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.AddField(
            model_name='watertest',
            name='well',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wellcom_app.Well'),
        ),
        migrations.AddField(
            model_name='notes',
            name='well',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wellcom_app.Well'),
        ),
        migrations.AddField(
            model_name='devicedata',
            name='well',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wellcom_app.Well'),
        ),
    ]
