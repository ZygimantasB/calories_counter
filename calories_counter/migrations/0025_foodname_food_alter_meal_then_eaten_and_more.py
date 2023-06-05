# Generated by Django 4.2 on 2023-06-05 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("calories_counter", "0024_remove_food_food_name_food_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="foodname",
            name="food",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="calories_counter.food",
            ),
        ),
        migrations.AlterField(
            model_name="meal",
            name="then_eaten",
            field=models.CharField(
                choices=[
                    ("supplements", "Supplements"),
                    ("breakfast", "Breakfast"),
                    ("before dinner", "Before Dinner"),
                    ("before workout", "Before Workout"),
                    ("snack", "Snack"),
                    ("lunch", "Lunch"),
                    ("before lunch", "Before Lunch"),
                    ("before sleep", "Before Sleep"),
                    ("dinner", "Dinner"),
                    ("after workout", "After Workout"),
                    ("other", "Other"),
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
