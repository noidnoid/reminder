# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-03 14:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20170703_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]