# Generated by Django 4.2 on 2023-06-07 18:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("food_information_app", "0002_auto_20230607_2154"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productinformation",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
