# Generated by Django 4.2 on 2023-06-07 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("calories_counter", "0036_alter_meal_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meal",
            name="user",
            field=models.ForeignKey(
                choices=[
                    ("before workout", "Before Workout"),
                    ("before lunch", "Before Lunch"),
                    ("breakfast", "Breakfast"),
                    ("other", "Other"),
                    ("lunch", "Lunch"),
                    ("supplements", "Supplements"),
                    ("dinner", "Dinner"),
                    ("after workout", "After Workout"),
                    ("before dinner", "Before Dinner"),
                    ("snack", "Snack"),
                    ("before sleep", "Before Sleep"),
                ],
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
