# Generated by Django 5.0 on 2024-03-19 06:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_post_desc_alter_post_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="desc",
            field=models.TextField(),
        ),
    ]
