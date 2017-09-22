# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-22 21:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('memeviewer', '0024_auto_20170908_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemeSourceImageOverride',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='File name')),
                ('disabled', models.BooleanField(default=False, verbose_name='Disabled')),
                ('add_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date added')),
                ('contexts', models.ManyToManyField(blank=True, to='memeviewer.MemeContext', verbose_name='Contexts')),
            ],
            options={
                'verbose_name': 'Source image override',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64, verbose_name='Key')),
                ('value', models.CharField(max_length=64, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Setting',
            },
        ),
    ]