# Generated by Django 4.2 on 2023-06-06 16:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("calories_counter", "0030_alter_meal_then_eaten_alter_userinformation_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meal",
            name="date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="meal",
            name="then_eaten",
            field=models.CharField(
                choices=[
                    ("before dinner", "Before Dinner"),
                    ("after workout", "After Workout"),
                    ("other", "Other"),
                    ("snack", "Snack"),
                    ("breakfast", "Breakfast"),
                    ("supplements", "Supplements"),
                    ("before workout", "Before Workout"),
                    ("before lunch", "Before Lunch"),
                    ("lunch", "Lunch"),
                    ("dinner", "Dinner"),
                    ("before sleep", "Before Sleep"),
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