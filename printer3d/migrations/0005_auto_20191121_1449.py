# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-11-21 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printer3d', '0004_auto_20191115_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer3d',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
