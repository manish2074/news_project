# Generated by Django 2.2.2 on 2019-11-15 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20191114_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_small_image', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('ad_small_image_updated', models.DateTimeField(auto_now_add=True)),
                ('ad_large_image', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('ad_large_image_updated', models.DateTimeField(auto_now_add=True)),
                ('ad_small_url', models.URLField(blank=True, max_length=270, null=True)),
                ('ad_large_url', models.URLField(blank=True, max_length=270, null=True)),
            ],
        ),
    ]
