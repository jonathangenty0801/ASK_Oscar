# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('analytics', '0030_auto_20170928_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_subscription',
            name='unsubcription_datetime',
            field=models.DateTimeField(blank=True),
        ),
    ]