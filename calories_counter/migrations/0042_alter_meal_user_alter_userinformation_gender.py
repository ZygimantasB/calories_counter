# Generated by Django 4.2 on 2023-06-12 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("calories_counter", "0041_alter_meal_user_alter_userinformation_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meal",
            name="user",
            field=models.ForeignKey(
                choices=[
                    ("breakfast", "Breakfast"),
                    ("other", "Other"),
                    ("supplements", "Supplements"),
                    ("after workout", "After Workout"),
                    ("before sleep", "Before Sleep"),
                    ("before dinner", "Before Dinner"),
                    ("dinner", "Dinner"),
                    ("before workout", "Before Workout"),
                    ("before lunch", "Before Lunch"),
                    ("lunch", "Lunch"),
                    ("snack", "Snack"),
                ],
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
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
