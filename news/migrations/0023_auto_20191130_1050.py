# Generated by Django 2.2.2 on 2019-11-30 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0022_auto_20191129_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(related_name='our_tag', to='news.Tag'),
        ),
    ]