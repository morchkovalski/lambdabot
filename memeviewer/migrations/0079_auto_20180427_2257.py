# Generated by Django 2.0 on 2018-04-27 20:57

from django.db import migrations, models
import django.db.models.deletion
import memeviewer.models


class Migration(migrations.Migration):

    dependencies = [
        ('memeviewer', '0078_auto_20180427_2141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='memecontext',
            options={},
        ),
        migrations.AlterModelOptions(
            name='memeimagepool',
            options={'verbose_name': 'Image pool'},
        ),
        migrations.RemoveIndex(
            model_name='memecontext',
            name='idx_context_mcount',
        ),
        migrations.RemoveField(
            model_name='meem',
            name='context_link',
        ),
        migrations.RemoveField(
            model_name='memesourceimage',
            name='contexts',
        ),
        migrations.RemoveField(
            model_name='memetemplate',
            name='contexts',
        ),
        migrations.AddField(
            model_name='memeimagepool',
            name='friendly_name',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='meem',
            name='number',
            field=models.IntegerField(default=memeviewer.models.next_meme_number, unique=True),
        ),
        migrations.AlterField(
            model_name='meem',
            name='source_images',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='memesourceimage',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='memesourceimage',
            name='friendly_name',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='memetemplate',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='memetemplate',
            name='bg_image_file',
            field=models.ImageField(blank=True, default=None, max_length=256, null=True, upload_to='templates/', verbose_name='Background'),
        ),
        migrations.AlterField(
            model_name='memetemplate',
            name='friendly_name',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='memetemplate',
            name='image_file',
            field=models.ImageField(blank=True, default=None, max_length=256, null=True, upload_to='templates/', verbose_name='Overlay'),
        ),
        migrations.AlterField(
            model_name='memetemplateslot',
            name='slot_order',
            field=models.IntegerField(choices=[(0, 'Blue'), (1, 'Yellow'), (2, 'Green'), (3, 'Red'), (4, 'Cyan'), (5, 'Orange'), (6, 'Lime'), (7, 'Pink'), (8, 'Purple'), (9, 'Brown'), (10, 'Black'), (11, 'White')], verbose_name='Slot group'),
        ),
        migrations.AlterField(
            model_name='memetemplateslot',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memeviewer.MemeTemplate'),
        ),
        migrations.AddIndex(
            model_name='memeimagepool',
            index=models.Index(fields=['name'], name='idx_imgpool'),
        ),
    ]
