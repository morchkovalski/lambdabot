# Generated by Django 2.0 on 2018-02-24 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0048_remove_discordmeem_sent_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discordserver',
            name='log_channel',
        ),
    ]
