# Generated by Django 2.0 on 2018-02-27 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memeviewer', '0041_auto_20180226_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='memetemplate',
            name='image_file',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='C:\\Users\\morchv\\Documents\\PycharmProjects\\lamdabotweb\\media\\lambdabot\\templates'),
        ),
    ]
