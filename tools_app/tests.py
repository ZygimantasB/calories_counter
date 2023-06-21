from django.test import TestCase
from .utils import HealthCalculator
from .form import BMIForm

# Create your tests here.


# Test Functions in HealthCalculator class for validation

class ValidateWaistTest(TestCase):

    def setUp(self) -> None:
        self.calculator = HealthCalculator()

    def test_validate_waist_negative(self):
        """
        Test validate waist negative
        """
        with self.assertRaises(ValueError):
            self.calculator.validate_waist(-50)

    def test_validate_waist_zero(self):
        """
        Test validate waist zero
        """
        with self.assertRaises(ValueError):
            self.calculator.validate_waist(0)

    def test_validate_waist_boundaries_positive(self):
        """
        Test validate waist boundaries positive
        """
        with self.assertRaises(ValueError):
            self.calculator.validate_waist(301)


class ValidateHipTest(TestCase):

    def setUp(self) -> None:
        self.calculator = HealthCalculator()

    def test_validate_hip_negative(self):
        """
        Test validate hip negative
        """
        with self.assertRaises(ValueError):
            self.calculator.validate_hip(-50)

    def test_validate_hip_zero(self):
        """
        Test validate hip zero
        """
        with self.assertRaises(ValueError):
            self.calculator.validate_hip(0)

    def test_validate_hip_boundaries_positive(self):
        """
        Test validate hip boundaries positive
        """
        with self.assertRaises(ValueError):
            self.calculator.validate_hip(301)


class ValidateAgeTest(TestCase):

    def setUp(self) -> None:
        self.calculator = HealthCalculator()

    def test_validate_age_negative(self):
        """
        Test validate age negative
        """
        with self.assertRaises(ValueError):
            self.calculator.validate_age(-50)

    def test_validate_age_zero(self):
        """
        Test validate age zero
        """
        with self.assertRaises(ValueError):
            self.calculator.validate_age(0)

    def test_validate_age_boundaries_positive(self):
        """
        Test validate age boundaries positive
        """
        with self.assertRaises(ValueError):
            self.calculator.validate_age(124)


class ValidateDurationMinutesTest(TestCase):

        def setUp(self):
            self.calculator = HealthCalculator()

        def test_validate_duration_minutes_negative(self):
            """
            Test validate duration minutes negative
            """
            with self.assertRaises(ValueError):
                self.calculator.validate_duration_minutes(-50)

        def test_validate_duration_minutes_zero(self):
            """
            Test validate duration minutes zero
            """
            with self.assertRaises(ValueError):
                self.calculator.validate_duration_minutes(0)

        def test_validate_duration_minutes_boundaries_positive(self):
            """
            Test validate duration minutes boundaries positive
            """
            with self.assertRaises(ValueError):
                self.calculator.validate_duration_minutes(1441)


class ValidateWeightTest(TestCase):

    def setUp(self):
        self.calculator = HealthCalculator()

    def test_validate_weight_negative(self):
        """
        Test validate weight negative
        """
        with self.assertRaises(ValueError):
            self.calculator.validate_weight(-50)

    def test_validate_weight_zero(self):
        """
        Test validate weight zero
        """
        with self.assertRaises(ValueError):
            self.calculator.validate_weight(0)

    def test_validate_weight_boundaries_positive(self):
        """
        Test validate weight boundaries positive
        """
        with self.assertRaises(ValueError):
            self.calculator.validate_weight(636)


class ValidateHeightTest(TestCase):

    def setUp(self):
        self.calculator = HealthCalculator()

    def test_validate_height_negative(self):
        """
        Test validate height negative
        """
        with self.assertRaises(ValueError):
            self.calculator.validate_height(-55)

    def test_validate_height_zero(self):
        """
        Test validate height zero
        """
        with self.assertRaises(ValueError):
            self.calculator.validate_height(0)

    def test_validate_height_boundaries_positive(self):
        """
        Test validate height boundaries positive
        """
        with self.assertRaises(ValueError):
            self.calculator.validate_height(273)


# Test Functions in HealthCalculator class


class WaistHipRatioTest(TestCase):

    def setUp(self):
        self.calculator = HealthCalculator()

    def test_waist_hip_ratio_waist_cm_negative(self):
        """
        Test waist hip ratio negative waist cm
        """
        with self.assertRaises(ValueError):
            self.calculator.waist_hip_ratio(-50, 50, 'male')

    def test_waist_hip_ratio_waist_cm_zero(self):
        """
        Test waist hip ratio zero waist cm
        """
        with self.assertRaises(ValueError):
            self.calculator.waist_hip_ratio(0, 50, 'male')

    def test_waist_hip_ratio_waist_cm_low_risk_boundaries_male(self):
        """
        Test waist hip ratio boundaries result 94 cm for Higher Risk (male)
        """
        result = self.calculator.waist_hip_ratio(93.81, 99.8, 'male')
        self.assertEqual(result, 'Your waist ratio is 94.0, you are at High Risk')

    def test_waist_hip_ratio_waist_cm_high_risk_male(self):
        """
        Test waist hip ratio for High Risk (male)
        """
        result = self.calculator.waist_hip_ratio(waist=98, hip=100, gender='male')
        self.assertEqual(result, 'Your waist ratio is 98.0, you are at High Risk')

    def test_waist_hip_ratio_waist_cm_high_risk_male_boundaries(self):
        """
        Test waist hip ratio boundaries result 99.99 cm for Higher Risk (male)
        """
        result = self.calculator.waist_hip_ratio(waist=99.98, hip=99.99, gender='male')
        self.assertEqual(result, 'Your waist ratio is 99.99, you are at High Risk')

    def test_waist_hip_ratio_waist_cm_increased_high_risk_male_boundaries(self):
        """
        Test waist hip ratio boundaries result 100 cm for Higher Risk (male)
        """
        result = self.calculator.waist_hip_ratio(waist=100, hip=100, gender='male')
        self.assertEqual(result, 'Your waist ratio is 100.0, you are at Increased Higher Risk')

    def test_waist_hip_ratio_low_risk_female(self):
        """
        Test waist hip ratio Low Risk (female)
        """
        result = self.calculator.waist_hip_ratio(waist=80, hip=110, gender='female')
        self.assertEqual(result, 'Your waist ratio is 72.73, you are at Low Risk')

    def test_waist_hip_ratio_high_risk_female_boundaries(self):
        """
        Test waist hip ratio boundaries result 80.0 cm for High Risk (female)
        """
        result = self.calculator.waist_hip_ratio(waist=80.24, hip=100.3, gender='female')
        self.assertEqual(result, 'Your waist ratio is 80.0, you are at High Risk')

    def test_waist_hip_ratio_high_risk_female(self):
        """
        Test waist hip ratio High Risk (female)
        """
        result = self.calculator.waist_hip_ratio(waist=80.24, hip=95, gender='female')
        self.assertEqual(result, 'Your waist ratio is 84.46, you are at High Risk')

    def test_waist_hip_ratio_increased_high_risk_female_boundaries(self):
        """
        Test waist hip ratio boundaries result 80.0 cm for Increased Higher Risk (female)
        """
        result = self.calculator.waist_hip_ratio(waist=80.24, hip=100.3, gender='female')
        self.assertEqual(result, 'Your waist ratio is 80.0, you are at High Risk')

    def test_waist_hip_ratio_increased_high_risk_female_boundaries_(self):
        """
        Test waist hip ratio boundaries result 89.99 cm for High risk(female)
        """
        result = self.calculator.waist_hip_ratio(waist=89.99, hip=100, gender='female')
        self.assertEqual(result, 'Your waist ratio is 89.99, you are at High Risk')

    def test_waist_hip_ratio_increased_high_risk_female(self):
        """
        Test waist hip ratio Increased Higher Risk (female)
        """
        result = self.calculator.waist_hip_ratio(waist=90, hip=89, gender='female')
        self.assertEqual(result, 'Your waist ratio is 101.12, you are at Increased Higher Risk')


class BasalMetabolicRateTest(TestCase):

    def setUp(self):
        self.calculator = HealthCalculator()

    def test_basal_metabolic_rate_weight_kg_negative(self):
        """
        Test basal metabolic rate negative age
        """
        with self.assertRaises(ValueError):
            self.calculator.basal_metabolic_rate('male', -50, 50, 80)

    def test_basal_metabolic_rate_weight_kg_zero(self):
        """
        Test basal metabolic rate zero age
        """
        with self.assertRaises(ValueError):
            self.calculator.basal_metabolic_rate('male', 0, 50, 80)

    def test_basal_metabolic_rate_weight_kg_boundaries(self):
        """
        Test basal metabolic rate zero age
        """
        with self.assertRaises(ValueError):
            self.calculator.basal_metabolic_rate('male', 700, 50, 80)

    def test_basal_metabolic_rate_height_cm_negative(self):
        """
        Test basal metabolic rate negative height cm
        """
        with self.assertRaises(ValueError):
            self.calculator.basal_metabolic_rate('male', 50, -50, 80)

    def test_basal_metabolic_rate_height_cm_zero(self):
        """
        Test basal metabolic rate zero height cm
        """
        with self.assertRaises(ValueError):
            self.calculator.basal_metabolic_rate('male', 50, 0, 80)

    def test_basal_metabolic_rate_height_cm_boundaries(self):
        """
        Test basal metabolic rate boundaries height cm
        """
        with self.assertRaises(ValueError):
            self.calculator.basal_metabolic_rate('male', 50, 1000, 80)

    def test_basal_metabolic_rate_age_negative(self):
        """
        Test basal metabolic rate negative age
        """
        with self.assertRaises(ValueError):
            self.calculator.basal_metabolic_rate('male', 50, 50, -80)

    def test_basal_metabolic_rate_age_zero(self):
        """
        Test basal metabolic rate zero age
        """
        with self.assertRaises(ValueError):
            self.calculator.basal_metabolic_rate('male', 50, 50, 0)

    def test_basal_metabolic_rate_age_boundaries(self):
        with self.assertRaises(ValueError):
            self.calculator.basal_metabolic_rate('male', 50, 50, 500)


class CalculateCaloriesBurnedTest(TestCase):

    def setUp(self) -> None:
        self.calculator = HealthCalculator()

    def test_calculate_calories_burned_weight_negative(self):
        """
        Test calculate calories burned negative weight
        """
        with self.assertRaises(ValueError):
            self.calculator.calculate_calories_burned("Sleeping", -50, 50)

    def test_calculate_calories_burned_weight_zero(self):
        """
        Test calculate calories burned zero weight
        """
        with self.assertRaises(ValueError):
            self.calculator.calculate_calories_burned("Sleeping", 0, 50)

    def test_calculate_calories_burned_duration_minutes_negative(self):
        """
        Test calculate calories burned negative duration minutes
        """
        with self.assertRaises(ValueError):
            self.calculator.calculate_calories_burned("Sleeping", 50, -50)

    def test_calculate_calories_burned_duration_minutes_zero(self):
        """
        Test calculate calories burned zero duration minutes
        """
        with self.assertRaises(ValueError):
            self.calculator.calculate_calories_burned("Sleeping", 50, 0)


class BMICalculatorTest(TestCase):
    def setUp(self):
        self.calculator = HealthCalculator()

    def test_bmi_calculator_underweight(self):
        """
        Test BMI calculator for underweight
        """
        result = self.calculator.bmi_calculator(weight_kg=50, height_cm=180)
        self.assertEqual(result, 'BMI: <u><b>15.43</b></u>, you are <u><b>Underweight</b></u>')

    def test_bmi_calculator_healthy_weight_boundaries(self):
        """
        Test BMI calculator for healthy weight boundaries
        """
        boundary_result = self.calculator.bmi_calculator(weight_kg=59.93, height_cm=180)
        self.assertEqual(boundary_result, 'BMI: <u><b>18.5</b></u>, you are <u><b>Healthy Weight</b></u>')

    def test_bmi_calculator_healthy_weight(self):
        """
        Test BMI calculator for healthy weight
        """
        result = self.calculator.bmi_calculator(weight_kg=70, height_cm=180)
        self.assertEqual(result, 'BMI: <u><b>21.6</b></u>, you are <u><b>Healthy Weight</b></u>')

    def test_bmi_calculator_overweight_boundaries(self):
        """
        Test BMI calculator for overweight boundaries
        """
        boundary_result = self.calculator.bmi_calculator(weight_kg=81, height_cm=180)
        self.assertEqual(boundary_result, 'BMI: <u><b>25.0</b></u>, you are <u><b>Overweight</b></u>')

    def test_bmi_calculator_overweight(self):
        """
        Test BMI calculator for overweight
        """
        result = self.calculator.bmi_calculator(weight_kg=90, height_cm=180)
        self.assertEqual(result, 'BMI: <u><b>27.78</b></u>, you are <u><b>Overweight</b></u>')

    def test_bmi_calculator_obesity_boundaries(self):
        """
        Test BMI calculator for obesity boundaries
        """
        boundary_result = self.calculator.bmi_calculator(weight_kg=96.97, height_cm=179.81)
        self.assertEqual(boundary_result, 'BMI: <u><b>29.99</b></u>, you are <u><b>Obesity</b></u>')

    def test_bmi_calculator_obesity(self):
        """
        Test BMI calculator for obesity
        """
        result = self.calculator.bmi_calculator(weight_kg=100, height_cm=180)
        self.assertEqual(result, 'BMI: <u><b>30.86</b></u>, you are <u><b>Obesity</b></u>')
