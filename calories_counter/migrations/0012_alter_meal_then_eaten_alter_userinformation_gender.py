# Generated by Django 4.2 on 2023-06-01 18:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("calories_counter", "0011_remove_userinformation_age_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meal",
            name="then_eaten",
            field=models.CharField(
                choices=[
                    ("before lunch", "Before Lunch"),
                    ("lunch", "Lunch"),
                    ("after workout", "After Workout"),
                    ("before sleep", "Before Sleep"),
                    ("before dinner", "Before Dinner"),
                    ("dinner", "Dinner"),
                    ("before workout", "Before Workout"),
                    ("breakfast", "Breakfast"),
                    ("other", "Other"),
                    ("snack", "Snack"),
                ],
                default="Snack",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="userinformation",
            name="gender",
            field=models.CharField(
                choices=[("male", "Male"), ("female", "Female")], max_length=6
            ),
        ),
    ]
