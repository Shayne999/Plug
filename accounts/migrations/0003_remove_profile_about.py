# Generated by Django 5.0.6 on 2024-05-25 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='about',
        ),
    ]
