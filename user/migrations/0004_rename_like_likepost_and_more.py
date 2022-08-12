# Generated by Django 4.0.3 on 2022-08-05 13:25

import datetime
from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_remove_profile_image_profile_location_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Like',
            new_name='LikePost',
        ),
        migrations.RenameField(
            model_name='likepost',
            old_name='likes',
            new_name='no_of_likes',
        ),
        migrations.AddField(
            model_name='post',
            name='no_of_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
