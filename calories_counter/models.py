from django.db import models

from django.contrib.auth.models import User

from datetime import date
from pygrowup import Calculator

from CONSTATNS.gender import GENDER

# Create your models here.


class Food(models.Model):
    """
    Food model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    then_eaten = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(null=True, blank=True)
    food_name = models.CharField(max_length=255, blank=True, null=True)
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    protein = models.DecimalField(max_digits=6, decimal_places=2)
    fat = models.DecimalField(max_digits=6, decimal_places=2)
    carbs = models.DecimalField(max_digits=6, decimal_places=2)
    weight_measure = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.food_name


class UserInformation(models.Model):
    """
    User information model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    gender = models.CharField(max_length=6, choices=GENDER)
    user_photo = models.ImageField(blank=True, null=True)

    @property
    def age(self):
        """
        Calculate age
        :return:
        """
        if self.date_of_birth:
            today = date.today()
            born = self.date_of_birth
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return None

    @property
    def bmi_counter(self):
        """
        Calculate BMI
        :return:
        """
        bmi_result = round((self.weight / self.height / self.height) * 10_000, 2)
        if bmi_result < 18.5:
            result = f'BMI: <u><b>{bmi_result}</b></u>, you are <u><b>Underweight</b></u>'
        elif 18.5 < bmi_result < 24.9:
            result = f'BMI: <u><b>{bmi_result}</b></u>, you are <u><b>Healthy Weight</b></u>'
        elif 25 < bmi_result < 29.9:
            result = f'BMI: <u><b>{bmi_result}</b></u>, you are <u><b>Overweight</b></u>'
        else:
            result = f'BMI: <u><b>{bmi_result}</b></u>, you are <u><b>Obesity</b></u>'
        return result

    def update_weight(self, new_weight):
        """
        Update weight
        :param new_weight:
        :return:
        """
        self.weight = new_weight
        self.save()
        WeightHistory.objects.create(user_information=self, weight=new_weight)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class WeightHistory(models.Model):
    """
    Weight history model
    """
    user_information = models.ForeignKey(UserInformation, on_delete=models.CASCADE, related_name='weight_histories')
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField()

    def __str__(self):
        return f"{self.user_information.first_name} {self.user_information.last_name} - {self.date}"


class BodyCircumferenceMeasurements(models.Model):
    """
    Body circumference measurements model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_now=True)
    neck_size = models.DecimalField(max_digits=6, decimal_places=2)
    chest_size = models.DecimalField(max_digits=6, decimal_places=2)
    waist_size = models.DecimalField(max_digits=6, decimal_places=2)
    left_bicep_size = models.DecimalField(max_digits=6, decimal_places=2)
    right_bicep_size = models.DecimalField(max_digits=6, decimal_places=2)
    left_forearm_size = models.DecimalField(max_digits=6, decimal_places=2)
    right_forearm_size = models.DecimalField(max_digits=6, decimal_places=2)
    left_thigh_size = models.DecimalField(max_digits=6, decimal_places=2)
    right_thigh_size = models.DecimalField(max_digits=6, decimal_places=2)
    left_calf_size = models.DecimalField(max_digits=6, decimal_places=2)
    right_calf_size = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.date} - Body Circumference Measurements"
