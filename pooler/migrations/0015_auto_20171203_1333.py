# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pooler', '0014_auto_20171203_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passengerprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='passenger/profile-pic/user-icon.png', upload_to='passenger/profile-pic'),
        ),
    ]
