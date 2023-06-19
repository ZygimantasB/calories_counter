from django.shortcuts import render
from django.views import View

from .form import BMIForm, WaitHipRatioForm, DailyCaloriesForm, BurnedCaloriesForm, BasalMetabolicRateForm, BodyFatForm

from .utils import HealthCalculator

# Create your views here.


health_calculator = HealthCalculator()


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
            bmi_result = health_calculator.bmi_calculator(weight, height)
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
            result = health_calculator.wait_hip_ratio(waist, hip, gender)

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

            bmr = health_calculator.basal_metabolic_rate(gender, weight_kg, height_cm, age)

            daily_calories = health_calculator.daily_calories(bmr, activity_level)

            return render(request, self.template_name, {'form': form,
                                                        'bmr': bmr,
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

            calories_burned = health_calculator.calculate_calories_burned(activity, weight_kg, duration_minutes)
            return render(request, self.template_name, {'form': form,
                                                        'calories_burned': calories_burned})
        else:
            return render(request, self.template_name, {'form': form})


class BasalMetabolicRate(View):
    template_name = "tools_app/basal_metabolic_rate.html"

    def get(self, request):
        form = BasalMetabolicRateForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BasalMetabolicRateForm(request.POST)
        print(form.errors)
        if form.is_valid():
            weight_kg = form.cleaned_data['weight_kg']
            height_cm = form.cleaned_data['height_cm']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']

            bmr_result = health_calculator.basal_metabolic_rate(gender, weight_kg, height_cm, age)

            return render(request, self.template_name, {'form': form,
                                                        'bmr_result': bmr_result})
        else:
            return render(request, self.template_name, {'form': form})


class CalculateBodyFat(View):
    template_name = "tools_app/calculation_body_fat.html"

    def get(self, request):
        form = BodyFatForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BodyFatForm(request.POST)
        if form.is_valid():
            weight_kg = form.cleaned_data['weight_kg']
            height_cm = form.cleaned_data['height_cm']
            waist_cm = form.cleaned_data['waist_cm']
            neck_cm = form.cleaned_data['neck_cm']
            gender = form.cleaned_data['gender']
            hip_cm = 0 if gender == 'male' else form.cleaned_data['hip_cm']

            body_fat_result = health_calculator.calculate_body_fat_percentage(gender, weight_kg, height_cm,
                                                                              waist_cm, neck_cm, hip_cm)

            return render(request, self.template_name, {'form': form,
                                                        'body_fat_result': body_fat_result})
        else:
            return render(request, self.template_name, {'form': form})
