# Generated by Django 4.2.1 on 2023-10-30 16:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="user",
        ),
        migrations.DeleteModel(
            name="Work",
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
