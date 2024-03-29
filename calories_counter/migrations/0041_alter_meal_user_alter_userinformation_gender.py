# Generated by Django 4.2 on 2023-06-08 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("calories_counter", "0040_alter_meal_user_alter_userinformation_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meal",
            name="user",
            field=models.ForeignKey(
                choices=[
                    ("before workout", "Before Workout"),
                    ("supplements", "Supplements"),
                    ("before dinner", "Before Dinner"),
                    ("dinner", "Dinner"),
                    ("before lunch", "Before Lunch"),
                    ("before sleep", "Before Sleep"),
                    ("breakfast", "Breakfast"),
                    ("after workout", "After Workout"),
                    ("snack", "Snack"),
                    ("lunch", "Lunch"),
                    ("other", "Other"),
                ],
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
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
