# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
