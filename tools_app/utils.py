from math import log10


class HealthCalculator:
    """
    Statless Class recomended if I don't need to store any state in the object.
    """
    MET_VALUES = {
        'sleeping': 0.9,
        'watching TV': 1,
        'writing, desk work, typing': 1.8,
        'walking, 5.63 kph': 4.3,
        'basketball, shooting baskets': 4.5,
        'bicycling, stationary, 50 watts, light effort': 5.5,
        'running, 8.05 kph (7.5 minute km)': 8,
        'jumping rope': 10,
        'running, 16.09 kph (3.7 min km)': 16
    }

    ACTIVITY_FACTORS = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725,
        'extra_active': 1.9
    }

    def bmi_calculator(self, weight_kg, height_cm):
        """
        Calculates BMI
        :param weight_kg:
        :param height_cm:
        :return:
        """
        bmi = round((weight_kg / height_cm / height_cm) * 10_000, 2)
        if bmi < 18.5:
            bmi_result = f'BMI: <u><b>{bmi}</b></u>, you are <u><b>Underweight</b></u>'
        elif bmi < 24.9:
            bmi_result = f'BMI: <u><b>{bmi}</b></u>, you are <u><b>Healthy Weight</b></u>'
        elif bmi < 29.9:
            bmi_result = f'BMI: <u><b>{bmi}</b></u>, you are <u><b>Overweight</b></u>'
        else:
            bmi_result = f'BMI: <u><b>{bmi}</b></u>, you are <u><b>Obesity</b></u>'
        return bmi_result

    def calculate_calories_burned(self, activity, weight_kg, duration_minutes):
        if activity not in self.MET_VALUES:
            return "Invalid activity. Please choose an activity from the list of available activities."

        met = self.MET_VALUES[activity]
        calories_per_minute = met * weight_kg * 3.5 / 200
        calories_burned = round(calories_per_minute * duration_minutes, 2)
        return calories_burned

    def basal_metabolic_rate(self, gender, weight_kg, height_cm, age):
        bmr = 0
        if gender == 'male':
            bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
        elif gender == 'female':
            bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
        return abs(bmr)

    def daily_calories(self, bmr, activity_level):
        activity_factor = 0
        if activity_level not in self.ACTIVITY_FACTORS:
            return "Invalid activity level. Please choose an activity level from the list of available activity levels."
        activity_factor = self.ACTIVITY_FACTORS[activity_level]
        daily_calories = abs(round(bmr * activity_factor, 2))
        return daily_calories

    def wait_hip_ratio(self, waist, hip, gender):
        waist_hip_ratio = waist / hip
        waist_hip_ratio = round(waist_hip_ratio * 100, 2)
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
        return result

    def calculate_body_fat_percentage(self, gender, weight_kg, height_cm, waist_cm, neck_cm, hip_cm=None):
        weight_lb = weight_kg * 2.20462
        height_in = height_cm * 0.393701
        waist_in = waist_cm * 0.393701
        neck_in = neck_cm * 0.393701
        hip_in = None
        if hip_cm:
            hip_in = hip_cm * 0.393701

        body_fat_percentage = 0

        if waist_in <= neck_in:
            raise ValueError("Waist measurement must be greater than neck measurement.")

        match gender:
            case 'male':
                body_fat_percentage = 86.010 * log10(waist_in - neck_in) - 70.041 * log10(height_in) + 36.76
            case 'female':
                body_fat_percentage = 163.205 * log10(waist_in + hip_in - neck_in) - 97.684 * log10(height_in) - 78.387
            case _:
                return 'You entered wrong information. Please try again.'
        return round(body_fat_percentage, 2)
