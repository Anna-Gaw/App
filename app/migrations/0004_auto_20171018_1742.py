# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 17:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20171018_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='food',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='food',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Food'),
        ),
    ]
