# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('analytics', '0038_auto_20171010_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='http_auth',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
