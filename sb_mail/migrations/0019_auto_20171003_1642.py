# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('sb_mail', '0018_auto_20171003_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sb_mail_server',
            name='priority',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]