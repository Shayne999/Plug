# Generated by Django 5.0.6 on 2024-05-28 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_profile_user'),
        ('feed', '0007_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorited_by', to='feed.post'),
        ),
    ]
