# Generated by Django 5.0.7 on 2024-07-15 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='preview',
            field=models.FileField(default=datetime.datetime.now, upload_to='videos/'),
        ),
    ]
