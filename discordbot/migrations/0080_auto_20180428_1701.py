# Generated by Django 2.0 on 2018-04-28 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0079_auto_20180428_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discordmeem',
            name='meme',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='memeviewer.Meem'),
        ),
    ]
