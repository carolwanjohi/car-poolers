# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 14:43
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pooler', '0007_auto_20171201_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='driver/profile-pic')),
                ('car_image', models.ImageField(blank=True, upload_to='car-image/')),
                ('car_capacity', models.PositiveIntegerField(blank=True, default=0)),
                ('car_number_plate', models.CharField(blank=True, max_length=60, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('car_color', models.CharField(blank=True, max_length=255)),
                ('gender', models.CharField(blank=True, choices=[('F', 'female'), ('M', 'male'), ('Both', 'both'), ('None', 'non-specified')], default='None', max_length=30)),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pooler.Driver')),
            ],
        ),
    ]
