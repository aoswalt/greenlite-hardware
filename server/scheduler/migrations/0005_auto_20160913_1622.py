# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_auto_20160913_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vertex',
            name='last_seen',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]