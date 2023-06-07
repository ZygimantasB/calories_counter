from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('food_information_app', '0001_initial'),  # or whatever the last migration was
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('serving_size', models.DecimalField(decimal_places=2, max_digits=6)),
                ('calories', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total_fat', models.DecimalField(decimal_places=2, max_digits=6)),
                ('protein', models.DecimalField(decimal_places=2, max_digits=6)),
                ('carbohydrate', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]