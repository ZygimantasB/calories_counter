# Generated by Django 4.2 on 2023-05-30 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "calories_counter",
            "0003_foods_meals_userinformation_remove_meal_foods_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="foods",
            name="meals_ID",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="calories_counter.meals",
            ),
        ),
        migrations.AddField(
            model_name="meals",
            name="then_eaten",
            field=models.CharField(
                choices=[
                    ("snack", "Snack"),
                    ("before dinner", "Before Dinner"),
                    ("after workout", "After Workout"),
                    ("dinner", "Dinner"),
                    ("lunch", "Lunch"),
                    ("breakfast", "Breakfast"),
                    ("other", "Other"),
                    ("before lunch", "Before Lunch"),
                    ("before sleep", "Before Sleep"),
                    ("before workout", "Before Workout"),
                ],
                default="BREAKFAST",
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
