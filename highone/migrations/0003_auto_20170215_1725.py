# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-15 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('highone', '0002_hobby'),
    ]

    operations = [
        migrations.AddField(
            model_name='hobby',
            name='modn',
            field=models.CharField(default='act', max_length=20),
        ),
        migrations.AddField(
            model_name='hobby',
            name='name',
            field=models.CharField(default='***', max_length=50),
        ),
        migrations.AddField(
            model_name='hobby',
            name='pric',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='hobby',
            name='prof',
            field=models.CharField(default='Dis', max_length=500),
        ),
        migrations.AddField(
            model_name='hobby',
            name='rank',
            field=models.CharField(default='0', max_length=5),
        ),
    ]
