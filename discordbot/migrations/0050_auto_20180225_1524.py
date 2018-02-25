# Generated by Django 2.0 on 2018-02-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0049_remove_discordserver_log_channel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discordcommand',
            name='custom_perm',
        ),
        migrations.RemoveField(
            model_name='discordcommand',
            name='denied_message',
        ),
        migrations.RemoveField(
            model_name='discordcommand',
            name='hidden',
        ),
        migrations.RemoveField(
            model_name='discordcommand',
            name='restricted',
        ),
        migrations.AddField(
            model_name='discordcommand',
            name='permission',
            field=models.IntegerField(blank=True, choices=[(1, 'Use cleverbot'), (2, 'Use murphybot')], default=None, null=True, verbose_name='Permission'),
        ),
        migrations.AddField(
            model_name='discordcommand',
            name='servers',
            field=models.ManyToManyField(blank=True, to='discordbot.DiscordServer', verbose_name='Servers'),
        ),
        migrations.AlterField(
            model_name='discordserverperm',
            name='permission',
            field=models.IntegerField(blank=True, choices=[(1, 'Use cleverbot'), (2, 'Use murphybot')], default=None, null=True, verbose_name='Permission'),
        ),
        migrations.AlterField(
            model_name='discordserveruserperm',
            name='permission',
            field=models.IntegerField(blank=True, choices=[(1, 'Use cleverbot'), (2, 'Use murphybot')], default=None, null=True, verbose_name='Permission'),
        ),
        migrations.DeleteModel(
            name='DiscordPerm',
        ),
    ]