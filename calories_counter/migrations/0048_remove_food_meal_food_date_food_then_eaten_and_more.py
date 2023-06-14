# Generated by Django 4.2 on 2023-06-14 05:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("calories_counter", "0047_alter_meal_then_eaten_alter_meal_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="food",
            name="meal",
        ),
        migrations.AddField(
            model_name="food",
            name="date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="food",
            name="then_eaten",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="userinformation",
            name="gender",
            field=models.CharField(
                choices=[("male", "Male"), ("female", "Female")], max_length=6
            ),
        ),
        migrations.DeleteModel(
            name="Meal",
        ),
    ]
