# Generated by Django 2.2.2 on 2019-11-12 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20191112_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, max_length=270, null=True),
        ),
    ]
