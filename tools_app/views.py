from django.shortcuts import render
from django.views import View

from .form import BMIForm, WaitHipRatioForm

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
