# Generated by Django 4.0.3 on 2022-07-16 16:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(blank=True)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2022, 7, 16, 16, 16, 53, 995053, tzinfo=utc))),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
