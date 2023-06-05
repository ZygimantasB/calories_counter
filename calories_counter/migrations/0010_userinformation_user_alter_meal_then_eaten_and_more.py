# Generated by Django 4.2 on 2023-06-01 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "calories_counter",
            "0009_remove_userinformation_user_userinformation_email_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="userinformation",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="meal",
            name="then_eaten",
            field=models.CharField(
                choices=[
                    ("before sleep", "Before Sleep"),
                    ("dinner", "Dinner"),
                    ("after workout", "After Workout"),
                    ("before lunch", "Before Lunch"),
                    ("before dinner", "Before Dinner"),
                    ("snack", "Snack"),
                    ("before workout", "Before Workout"),
                    ("breakfast", "Breakfast"),
                    ("other", "Other"),
                    ("lunch", "Lunch"),
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