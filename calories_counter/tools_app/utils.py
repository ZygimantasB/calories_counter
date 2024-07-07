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

    @staticmethod
    def validate_weight(weight_kg: float) -> None:
        """
        Validates weight input
        :param weight_kg: weight in kg
        """
        if weight_kg <= 0:
            raise ValueError("Your are in space ? Please enter a positive number for weight.")
        elif weight_kg > 635:
            raise ValueError("Enter realistic number. Heaviest person in the world was Jon Brower Minnoch 635 kg")

    @staticmethod
    def validate_height(height_cm: float) -> None:
        """
        Validates height input
        :param height_cm: height in cm
        """
        if height_cm <= 0:
            raise ValueError("Your are in space ?  Please enter a positive number for height.")
        elif height_cm > 272:
            raise ValueError("Enter realistic number. Tallest person in the world was Robert Wadlow 272 cm.")

    @staticmethod
    def validate_duration_minutes(duration_minutes: int) -> None:
        """
        Validates duration input
        :param duration_minutes: duration in minutes
        """
        if duration_minutes <= 0:
            raise ValueError("Invalid input. Please enter a positive number for duration.")
        elif duration_minutes > 1440:
            raise ValueError("Enter realistic number.")

    @staticmethod
    def validate_age(age: int) -> None:
        """
        Validates age input
        :param age: age in years
        """
        if age <= 0:
            raise ValueError("Invalid input. Please enter a positive number for age.")
        elif age > 122:
            raise ValueError("You can`t be that old. Oldest person in the world was Jeanne Calment 122 years.")

    @staticmethod
    def validate_waist(waist: float) -> None:
        """
        Validates waist input
        :param waist: waist in cm
        """
        if waist <= 0:
            raise ValueError("Invalid input. Please enter a positive number for waist.")
        elif waist > 300:
            raise ValueError("Enter realistic number.")

    @staticmethod
    def validate_hip(hip: float) -> None:
        """
        Validates hip input
        :param hip: hip in cm
        """
        if hip <= 0:
            raise ValueError("Invalid input. Please enter a positive number for hip.")
        elif hip > 300:
            raise ValueError("Enter realistic number.")

    @staticmethod
    def validate_hip_female(hip: float, gender: str = 'female') -> None:
        """
        Validates hip input
        :param gender:
        :param hip:
        :return:
        """
        if hip is None:
            hip = 1
        elif hip <= 0 and gender == 'female':
            hip = 1
        elif hip > 300 and gender == 'female':
            raise ValueError("Enter realistic number.")

    @staticmethod
    def validate_hip_male(hip: int = 1, gender: str = 'male') -> int:
        """
        Validates hip input
        :param gender:
        :param hip:
        :return:
        """
        return hip

    @staticmethod
    def validate_neck(neck_cm: float) -> None:
        """
        Validates neck input
        :param neck_cm: wrist in cm
        """
        if neck_cm <= 0:
            raise ValueError("Invalid input. Please enter a positive number for wrist.")
        elif neck_cm > 100:
            raise ValueError("Enter realistic number.")

    @staticmethod
    def unit_conversion(weight_lb: float, height_in: float, waist_in: float, neck_in: float,
                        hip_in: float = 0) -> tuple:
        """
        This view is for converting units.
        :param weight_lb:
        :param height_in:
        :param waist_in:
        :param neck_in:
        :param hip_in:
        :return:
        """
        weight_kg = weight_lb / 2.20462
        height_cm = height_in / 0.393701
        waist_cm = waist_in / 0.393701
        neck_cm = neck_in / 0.393701
        hip_cm = hip_in / 0.393701
        return weight_kg, height_cm, waist_cm, neck_cm, hip_cm

    def bmi_calculator(self, weight_kg: float, height_cm: float) -> str:
        """
        Calculates BMI (Body Mass Index) based on weight and height.
        :param weight_kg: weight in kg
        :param height_cm: height in cm
        :return: BMI result
        """
        self.validate_weight(weight_kg)
        self.validate_height(height_cm)

        bmi = round((weight_kg / height_cm / height_cm) * 10_000, 2)

        if bmi < 18.5:
            bmi_result = f'BMI: <u><b>{bmi}</b></u>, you are <u><b>Underweight</b></u>'
        elif bmi < 25.0:
            bmi_result = f'BMI: <u><b>{bmi}</b></u>, you are <u><b>Healthy Weight</b></u>'
        elif bmi < 29.9:
            bmi_result = f'BMI: <u><b>{bmi}</b></u>, you are <u><b>Overweight</b></u>'
        else:
            bmi_result = f'BMI: <u><b>{bmi}</b></u>, you are <u><b>Obesity</b></u>'
        return bmi_result

    def calculate_calories_burned(self, activity: str, weight_kg: float, duration_minutes: int) -> float:
        """
        Calculates calories burned based on activity, weight and duration.
        :param activity:
        :param weight_kg:
        :param duration_minutes:
        :return: calories_burned
        """

        self.validate_weight(weight_kg)
        self.validate_duration_minutes(duration_minutes)

        met = self.MET_VALUES[activity]
        calories_per_minute = met * weight_kg * 3.5 / 200
        calories_burned = round(calories_per_minute * duration_minutes, 2)
        return calories_burned

    def basal_metabolic_rate(self, gender: str, weight_kg: float, height_cm: float, age: int) -> float:
        """
        This view is for calculating Basal Metabolic Rate.
        :param gender:
        :param weight_kg:
        :param height_cm:
        :param age:
        :return bmr:
        """
        self.validate_weight(weight_kg)
        self.validate_height(height_cm)
        self.validate_age(age)

        bmr = 0
        if gender == 'male':
            bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
        elif gender == 'female':
            bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
        return abs(bmr)

    def daily_calories(self, bmr: float, activity_level: str) -> float:
        """
        This view is for calculating Daily Calories.
        :param bmr:
        :param activity_level:
        :return:
        """
        activity_factor = self.ACTIVITY_FACTORS[activity_level]
        daily_calories = abs(round(bmr * activity_factor, 2))
        return daily_calories

    def waist_hip_ratio(self, waist: float, hip: float, gender: str) -> str:
        """
        This view is for calculating Waist Hip Ratio.
        :param waist:
        :param hip:
        :param gender:
        :return:
        """
        self.validate_waist(waist)
        self.validate_hip(hip)

        waist_hip_ratio = waist / hip
        waist_hip_ratio = round(waist_hip_ratio * 100, 2)
        result = ''
        match gender:
            case 'male':
                if waist_hip_ratio < 94:
                    result = f"Your waist ratio is {waist_hip_ratio}, you are at Low Risk"
                elif waist_hip_ratio <= 99.99:
                    result = f"Your waist ratio is {waist_hip_ratio}, you are at High Risk"
                else:
                    result = f"Your waist ratio is {waist_hip_ratio}, you are at Increased Higher Risk"
            case 'female':
                if waist_hip_ratio < 80:
                    result = f"Your waist ratio is {waist_hip_ratio}, you are at Low Risk"
                elif waist_hip_ratio <= 89.99:
                    result = f"Your waist ratio is {waist_hip_ratio}, you are at High Risk"
                else:
                    result = f"Your waist ratio is {waist_hip_ratio}, you are at Increased Higher Risk"
        return result

    def calculate_body_fat_percentage(self, gender: str, weight_kg: float, height_cm: float, waist_cm: float,
                                      neck_cm: float, hip_cm: float = 0) -> float:
        """
        This view is for calculating Body Fat Percentage.
        :param gender:
        :param weight_kg:
        :param height_cm:
        :param waist_cm:
        :param neck_cm:
        :param hip_cm:
        :return:
        """
        weight_lb, height_in, waist_in, neck_in, hip_in = self.unit_conversion(weight_kg, height_cm, waist_cm, neck_cm,
                                                                               hip_cm)

        self.validate_weight(weight_kg)
        self.validate_height(height_cm)
        self.validate_waist(waist_cm)
        self.validate_neck(neck_cm)
        self.validate_hip_female(hip_cm, gender='female')
        self.validate_hip_male()

        if hip_cm:
            hip_in = hip_cm * 0.393701

        body_fat_percentage = 0

        try:
            if waist_in - neck_in <= 0 or height_in <= 0:
                raise ValueError("Invalid input. Please check your measurements.")

            match gender:
                case 'male':
                    body_fat_percentage = 86.010 * log10(waist_in - neck_in) - 70.041 * log10(height_in) + 36.76
                case 'female':
                    body_fat_percentage = 163.205 * log10(waist_in + hip_in - neck_in) - 97.684 * log10(height_in) \
                                          - 78.387

        except ValueError as e:
            print("Error in calculate_body_fat_percentage: ", e)
            body_fat_percentage = 0

        return round(body_fat_percentage, 2)
