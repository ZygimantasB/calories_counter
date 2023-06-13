# Generated by Django 4.2 on 2023-06-12 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("calories_counter", "0042_alter_meal_user_alter_userinformation_gender"),
    ]

    operations = [
        migrations.CreateModel(
            name="BodyCircumferenceMeasurements",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("neck_size", models.DecimalField(decimal_places=2, max_digits=6)),
                ("chest_size", models.DecimalField(decimal_places=2, max_digits=6)),
                ("waist_size", models.DecimalField(decimal_places=2, max_digits=6)),
                (
                    "left_bicep_size",
                    models.DecimalField(decimal_places=2, max_digits=6),
                ),
                (
                    "right_bicep_size",
                    models.DecimalField(decimal_places=2, max_digits=6),
                ),
                (
                    "left_forearm_size",
                    models.DecimalField(decimal_places=2, max_digits=6),
                ),
                (
                    "right_forearm_size",
                    models.DecimalField(decimal_places=2, max_digits=6),
                ),
                (
                    "left_thigh_size",
                    models.DecimalField(decimal_places=2, max_digits=6),
                ),
                (
                    "right_thigh_size",
                    models.DecimalField(decimal_places=2, max_digits=6),
                ),
                ("left_calf_size", models.DecimalField(decimal_places=2, max_digits=6)),
                (
                    "right_calf_size",
                    models.DecimalField(decimal_places=2, max_digits=6),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="meal",
            name="user",
            field=models.ForeignKey(
                choices=[
                    ("dinner", "Dinner"),
                    ("before sleep", "Before Sleep"),
                    ("snack", "Snack"),
                    ("before workout", "Before Workout"),
                    ("other", "Other"),
                    ("before lunch", "Before Lunch"),
                    ("lunch", "Lunch"),
                    ("before dinner", "Before Dinner"),
                    ("after workout", "After Workout"),
                    ("supplements", "Supplements"),
                    ("breakfast", "Breakfast"),
                ],
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]