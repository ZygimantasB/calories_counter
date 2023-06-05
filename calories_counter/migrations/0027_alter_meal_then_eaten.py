# Generated by Django 4.2 on 2023-06-05 19:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("calories_counter", "0026_remove_food_name_food_food_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meal",
            name="then_eaten",
            field=models.CharField(
                choices=[
                    ("lunch", "Lunch"),
                    ("after workout", "After Workout"),
                    ("dinner", "Dinner"),
                    ("breakfast", "Breakfast"),
                    ("before dinner", "Before Dinner"),
                    ("other", "Other"),
                    ("before lunch", "Before Lunch"),
                    ("snack", "Snack"),
                    ("supplements", "Supplements"),
                    ("before workout", "Before Workout"),
                    ("before sleep", "Before Sleep"),
                ],
                default="Snack",
                max_length=50,
            ),
        ),
    ]
