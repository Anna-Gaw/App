# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
