# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 12:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('sb_shortlink', '0004_auto_20171012_1424'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Link',
        ),
    ]
