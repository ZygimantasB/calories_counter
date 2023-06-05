# Generated by Django 4.2 on 2023-06-05 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("calories_counter", "0027_alter_meal_then_eaten_alter_userinformation_gender"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="food",
            name="food_name",
        ),
        migrations.AlterField(
            model_name="meal",
            name="then_eaten",
            field=models.CharField(
                choices=[
                    ("snack", "Snack"),
                    ("supplements", "Supplements"),
                    ("before dinner", "Before Dinner"),
                    ("other", "Other"),
                    ("after workout", "After Workout"),
                    ("breakfast", "Breakfast"),
                    ("lunch", "Lunch"),
                    ("dinner", "Dinner"),
                    ("before lunch", "Before Lunch"),
                    ("before sleep", "Before Sleep"),
                    ("before workout", "Before Workout"),
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
        migrations.AddField(
            model_name="food",
            name="food_name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="food_name",
                to="calories_counter.foodname",
            ),
        ),
    ]
