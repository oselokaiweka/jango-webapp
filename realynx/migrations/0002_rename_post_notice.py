# Generated by Django 5.0.6 on 2024-07-03 15:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("realynx", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Post",
            new_name="Notice",
        ),
    ]
