# Generated by Django 4.0.3 on 2022-07-23 11:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_post_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 23, 11, 46, 8, 277659, tzinfo=utc)),
        ),
    ]
