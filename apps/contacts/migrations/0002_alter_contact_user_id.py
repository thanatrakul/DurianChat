# Generated by Django 5.0.10 on 2024-12-23 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="user_id",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]