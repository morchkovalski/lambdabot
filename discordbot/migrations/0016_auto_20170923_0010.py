# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-22 22:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0015_auto_20170922_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='discordmeem',
            name='channel_id',
            field=models.CharField(default='0', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discordmeem',
            name='sent_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date sent'),
        ),
    ]
