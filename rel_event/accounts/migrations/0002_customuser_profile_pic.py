# Generated by Django 4.2.8 on 2024-02-01 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="profile_pic",
            field=models.ImageField(blank=True, null=True, upload_to="user_pics/"),
        ),
    ]