# Generated by Django 4.2.10 on 2024-03-09 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagemodel",
            name="image",
            field=models.ImageField(
                blank=True,
                upload_to="catalog/",
                verbose_name="Будет приведено к ширине 1280px",
            ),
        ),
    ]
