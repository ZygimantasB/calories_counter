# Generated by Django 4.2 on 2023-06-08 16:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("food_information_app", "0003_alter_productinformation_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="productinformation",
            name="usage_count",
            field=models.IntegerField(default=0),
        ),
    ]
