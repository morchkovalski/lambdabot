# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-25 00:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memeviewer', '0014_remove_imageincontext_context'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('token', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='imageincontext',
            name='context_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memeviewer.MemeContext'),
        ),
        migrations.AlterField(
            model_name='meem',
            name='context_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memeviewer.MemeContext'),
        ),
        migrations.AlterField(
            model_name='meem',
            name='template_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memeviewer.MemeTemplate'),
        ),
    ]
