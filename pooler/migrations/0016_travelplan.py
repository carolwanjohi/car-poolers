# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 08:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pooler', '0015_auto_20171203_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_location', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('driver_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pooler.DriverProfile')),
            ],
        ),
    ]