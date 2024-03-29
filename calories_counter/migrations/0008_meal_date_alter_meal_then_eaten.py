# Generated by Django 4.2 on 2023-05-31 16:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("calories_counter", "0007_remove_meal_meal_datetime_alter_meal_then_eaten"),
    ]

    operations = [
        migrations.AddField(
            model_name="meal",
            name="date",
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="meal",
            name="then_eaten",
            field=models.CharField(
                choices=[
                    ("lunch", "Lunch"),
                    ("breakfast", "Breakfast"),
                    ("dinner", "Dinner"),
                    ("other", "Other"),
                    ("snack", "Snack"),
                    ("before sleep", "Before Sleep"),
                    ("before dinner", "Before Dinner"),
                    ("before workout", "Before Workout"),
                    ("before lunch", "Before Lunch"),
                    ("after workout", "After Workout"),
                ],
                default="Snack",
                max_length=50,
            ),
        ),
    ]
