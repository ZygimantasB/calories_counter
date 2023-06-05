# Generated by Django 4.2 on 2023-06-05 19:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("calories_counter", "0029_alter_meal_then_eaten_alter_userinformation_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meal",
            name="then_eaten",
            field=models.CharField(
                choices=[
                    ("supplements", "Supplements"),
                    ("after workout", "After Workout"),
                    ("snack", "Snack"),
                    ("dinner", "Dinner"),
                    ("lunch", "Lunch"),
                    ("before sleep", "Before Sleep"),
                    ("before lunch", "Before Lunch"),
                    ("other", "Other"),
                    ("before dinner", "Before Dinner"),
                    ("before workout", "Before Workout"),
                    ("breakfast", "Breakfast"),
                ],
                default="Snack",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="userinformation",
            name="gender",
            field=models.CharField(
                choices=[("female", "Female"), ("male", "Male")], max_length=6
            ),
        ),
    ]
