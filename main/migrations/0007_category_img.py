# Generated by Django 5.0 on 2024-03-19 07:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_alter_post_desc"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="img",
            field=models.ImageField(default="default.jpg", upload_to="categories"),
            preserve_default=False,
        ),
    ]