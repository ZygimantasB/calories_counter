# Generated by Django 4.2 on 2023-06-07 18:53

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductInformation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("serving_size", models.DecimalField(decimal_places=2, max_digits=6)),
                ("calories", models.DecimalField(decimal_places=2, max_digits=6)),
                ("total_fat", models.DecimalField(decimal_places=2, max_digits=6)),
                ("protein", models.DecimalField(decimal_places=2, max_digits=6)),
                ("carbohydrate", models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]