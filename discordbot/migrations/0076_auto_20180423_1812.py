# Generated by Django 2.0 on 2018-04-23 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0075_auto_20180423_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='discordserver',
            name='blacklisted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='discordserveruser',
            name='blacklisted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='discorduser',
            name='blacklisted',
            field=models.BooleanField(default=False),
        ),
    ]