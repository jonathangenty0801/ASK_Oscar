# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-19 05:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('taskoftheday', '0009_auto_20170819_0535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertaskhistory',
            old_name='guide_id',
            new_name='guide',
        ),
        migrations.RenameField(
            model_name='usertaskhistory',
            old_name='step_id',
            new_name='step',
        ),
        migrations.RenameField(
            model_name='usertaskhistory',
            old_name='task_id',
            new_name='task',
        ),
    ]
