# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-09 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('analytics', '0015_profile_connected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='connected',
            field=models.BooleanField(default=False),
        ),
    ]
