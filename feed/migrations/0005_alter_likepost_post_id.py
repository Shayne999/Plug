# Generated by Django 5.0.6 on 2024-05-28 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_rename_user_likepost_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likepost',
            name='post_id',
            field=models.UUIDField(),
        ),
    ]