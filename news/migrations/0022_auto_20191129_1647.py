# Generated by Django 2.2.2 on 2019-11-29 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0021_auto_20191129_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='tag',
            new_name='tags',
        ),
    ]
