# Generated by Django 2.2.2 on 2019-09-21 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20190921_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_image', models.ImageField(upload_to='uploads')),
                ('content', models.CharField(max_length=200)),
            ],
        ),
    ]
