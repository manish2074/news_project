# Generated by Django 2.2.2 on 2019-11-25 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20191125_0945'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AlterField(
            model_name='news',
            name='video_image',
            field=models.ImageField(blank=True, default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='video_title',
            field=models.CharField(blank=True, default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='video_url',
            field=models.URLField(blank=True, max_length=270),
        ),
    ]
