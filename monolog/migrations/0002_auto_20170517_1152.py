# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-17 03:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monolog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalog',
            old_name='catalogcode',
            new_name='catalog_code',
        ),
        migrations.RenameField(
            model_name='catalog',
            old_name='catalogname',
            new_name='catalog_name',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='subjectcode',
            new_name='subject_code',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='subjectname',
            new_name='subject_name',
        ),
    ]
