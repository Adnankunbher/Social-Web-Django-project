# Generated by Django 4.0.3 on 2022-08-06 06:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_post_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 6, 6, 58, 12, 97633, tzinfo=utc)),
        ),
    ]
