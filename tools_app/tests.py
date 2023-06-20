from django.test import TestCase
from .utils import HealthCalculator
from .form import BMIForm

# Create your tests here.


# Test Functions in HealthCalculator class for validation

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
        boundary_result = self.calculator.bmi_calculator(weight_kg=96.88, height_cm=180)
        self.assertEqual(boundary_result, 'BMI: <u><b>29.9</b></u>, you are <u><b>Obesity</b></u>')

    def test_bmi_calculator_obesity(self):
        """
        Test BMI calculator for obesity
        """
        result = self.calculator.bmi_calculator(weight_kg=100, height_cm=180)
        self.assertEqual(result, 'BMI: <u><b>30.86</b></u>, you are <u><b>Obesity</b></u>')


# Form tests


class BMIFormTest(TestCase):

    def setUp(self):
        self.form = BMIForm()

    def test_form_has_fields(self):
        """
        Test form has fields weight_kg and height_cm
        """
        expected = ['weight_kg', 'height_cm']
        actual = list(self.form.fields)
        self.assertSequenceEqual(expected, actual)

    def test_form_validation(self):
        """
        Test form validation
        """
        form = BMIForm(data={'weight_kg': 50, 'height_cm': 180})
        self.assertTrue(form.is_valid())

    def test_form_validation_fails_weight(self):
        """
        Test form validation fails when weight is 0
        """
        form_data = {'weight_kg': 0, 'height_cm': 180}
        form = BMIForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_validation_fails_height(self):
        """
        Test form validation fails when height is 0
        """
        form_data = {'weight_kg': 70, 'height_cm': 0}
        form = BMIForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_validation_fails_weight_and_height(self):
        """
        Test form validation fails when weight and height are 0
        """
        form_data = {'weight_kg': 0, 'height_cm': 0}
        form = BMIForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_validation_fails_weight_and_height_negative(self):
        """
        Test form validation fails when weight and height are negative
        """
        form_data = {'weight_kg': -1, 'height_cm': -1}
        form = BMIForm(data=form_data)
        self.assertFalse(form.is_valid())
