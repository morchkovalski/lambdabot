# Generated by Django 2.0 on 2017-12-27 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0039_auto_20171227_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='discordpermission',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='discordpermission',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Permission'),
        ),
    ]
