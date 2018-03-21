# Generated by Django 2.0 on 2018-03-21 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memeviewer', '0053_auto_20180321_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memetemplateslot',
            name='slot_order',
            field=models.IntegerField(choices=[(0, 'Black'), (1, 'Brown'), (2, 'Red'), (3, 'Orange'), (4, 'Yellow'), (5, 'Lime'), (6, 'Green'), (7, 'Cyan'), (8, 'Blue'), (9, 'Purple'), (10, 'Pink'), (11, 'White')], verbose_name='Slot flavor'),
        ),
    ]
