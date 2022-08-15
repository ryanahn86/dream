# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-11-15 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printer3d', '0003_auto_20191109_0925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='printer3d',
            name='status',
        ),
        migrations.AddField(
            model_name='printer3d',
            name='reservation_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='printer3d',
            name='reservation_start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='printer3d',
            name='reservation_status',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='printer3d',
            name='reservation_user_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='printer3d',
            name='reservation_user_email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='printer3d',
            name='reservation_user_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='printer3d',
            name='reservation_user_phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]