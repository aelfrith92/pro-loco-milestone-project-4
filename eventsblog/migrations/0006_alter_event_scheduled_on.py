# Generated by Django 3.2.15 on 2022-08-27 10:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eventsblog', '0005_auto_20220822_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='scheduled_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 10, 10, 8, 6, 307685, tzinfo=utc)),
        ),
    ]
