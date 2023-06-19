from django.shortcuts import render
from django.views import View

from .form import BMIForm, WaitHipRatioForm, DailyCaloriesForm, BurnedCaloriesForm

from .utils import calculate_calories_burned

# Create your views here.


class CalculateBMI(View):
    template_name = "tools_app/calculation_bmi.html"

    def get(self, request):
        form = BMIForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BMIForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            bmi = round((weight / height / height) * 10_000, 2)
            if bmi < 18.5:
                bmi_result = f'BMI: <u><b>{bmi}</b></u>, you are <u><b>Underweight</b></u>'
            elif 18.5 < bmi < 24.9:
                bmi_result = f'BMI: <u><b>{bmi}</b></u>, you are <u><b>Healthy Weight</b></u>'
            elif 25 < bmi < 29.9:
                bmi_result = f'BMI: <u><b>{bmi}</b></u>, you are <u><b>Overweight</b></u>'
            else:
                bmi_result = f'BMI: <u><b>{bmi}</b></u>, you are <u><b>Obesity</b></u>'
            return render(request, self.template_name, {'form': form, 'bmi_result': bmi_result})
        return render(request, self.template_name, {'form': form}, )


class CalculateWaistHipRatio(View):
    template_name = "tools_app/calculation_waist_hip_ratio.html"

    def get(self, request):
        form = WaitHipRatioForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = WaitHipRatioForm(request.POST)
        if form.is_valid():
            waist = form.cleaned_data['waist']
            hip = form.cleaned_data['hip']
            gender = form.cleaned_data['gender']
            waist_hip_ratio = round(waist / hip, 2)
            waist_hip_ratio = waist_hip_ratio * 100
            result = ''
            match gender:
                case 'male':
                    if waist_hip_ratio < 94:
                        result = f"Your waist ratio is {waist_hip_ratio}, you are at Low Risk"
                    elif 94 <= waist_hip_ratio <= 99:
                        result = f"Your waist ratio is {waist_hip_ratio}, you are at High Risk"
                    else:
                        result = f"Your waist ratio is {waist_hip_ratio}, you are at Increased Higher Risk"
                case 'female':
                    if waist_hip_ratio <= 80:
                        result = f"Your waist ratio is {waist_hip_ratio}, you are at Low Risk"
                    elif 81 < waist_hip_ratio <= 89:
                        result = f"Your waist ratio is {waist_hip_ratio}, you are at High Risk"
                    else:
                        result = f"Your waist ratio is {waist_hip_ratio}, you are at Increased Higher Risk"

            return render(request, self.template_name, {'form': form, 'result': result})
        return render(request, self.template_name, {'form': form})


class CalculateDailyCalories(View):
    template_name = "tools_app/calculation_daily_calories.html"

    def get(self, request):
        form = DailyCaloriesForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = DailyCaloriesForm(request.POST)
        if form.is_valid():
            weight_kg = form.cleaned_data['weight_kg']
            height_cm = form.cleaned_data['height_cm']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            activity_level = form.cleaned_data['activity_level']
            bmr = 0
            activity_factor = 0
            if gender == 'male':
                bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
            elif gender == 'female':
                bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

            match activity_level:
                case 'sedentary':
                    activity_factor = 1.2
                case 'lightly_active':
                    activity_factor = 1.375
                case 'moderately_active':
                    activity_factor = 1.55
                case 'very_active':
                    activity_factor = 1.725
                case 'extra_active':
                    activity_factor = 1.9

            daily_calories = abs(round(bmr * activity_factor, 2))

            return render(request, self.template_name, {'form': form,
                                                        'bmr': bmr,
                                                        'activity_factor': activity_factor,
                                                        'daily_calories': daily_calories, })
        return render(request, self.template_name, {'form': form})


class CalculateBurnedCalories(View):
    template_name = "tools_app/calculation_burned_calories.html"

    def get(self, request):
        form = BurnedCaloriesForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BurnedCaloriesForm(request.POST)
        if form.is_valid():
            weight_kg = form.cleaned_data['weight_kg']
            duration_minutes = form.cleaned_data['duration_minutes']
            activity = form.cleaned_data['activity']

            print(f"Form data received: Weight - {weight_kg}, Activity - {activity}, Duration - {duration_minutes}")
            calories_burned = calculate_calories_burned(activity, weight_kg, duration_minutes)
            return render(request, self.template_name, {'form': form,
                                                        'calories_burned': calories_burned})
        else:
            return render(request, self.template_name, {'form': form})

