# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('analytics', '0023_profile_profile_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_rank',
            field=models.IntegerField(default=0),
        ),
    ]
