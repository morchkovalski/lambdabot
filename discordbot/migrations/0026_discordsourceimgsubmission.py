# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-29 22:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memeviewer', '0026_auto_20170929_2259'),
        ('discordbot', '0025_auto_20170929_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordSourceImgSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourceimg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memeviewer.MemeSourceImageOverride', verbose_name='Source image')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='discordbot.DiscordServerUser', verbose_name='Server user')),
            ],
            options={
                'verbose_name': 'Source image submission',
            },
        ),
    ]
