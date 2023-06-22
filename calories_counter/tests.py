from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import BodyCircumferenceMeasurements
from decimal import Decimal

# Create your tests here.


# test for BodyCircumferenceMeasurements model labels


class BodyCircumferenceMeasurementsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='testuser', password='12345')
        BodyCircumferenceMeasurements.objects.create(
            user=test_user,
            neck_size=12.00,
            chest_size=34.00,
            waist_size=28.00,
            left_bicep_size=11.00,
            right_bicep_size=11.00,
            left_forearm_size=10.00,
            right_forearm_size=10.00,
            left_thigh_size=22.00,
            right_thigh_size=22.00,
            left_calf_size=15.00,
            right_calf_size=15.00
        )

    def test_neck_size_label(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_label = measurement._meta.get_field('neck_size').verbose_name
        self.assertEquals(field_label, 'neck size')

    def test_chest_size_label(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_label = measurement._meta.get_field('chest_size').verbose_name
        self.assertEquals(field_label, 'chest size')

    def test_waist_size_label(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_label = measurement._meta.get_field('waist_size').verbose_name
        self.assertEquals(field_label, 'waist size')

    def test_left_bicep_size_label(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_label = measurement._meta.get_field('left_bicep_size').verbose_name
        self.assertEquals(field_label, 'left bicep size')

    def test_right_bicep_size_label(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_label = measurement._meta.get_field('right_bicep_size').verbose_name
        self.assertEquals(field_label, 'right bicep size')

    def test_left_forearm_size_label(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_label = measurement._meta.get_field('left_forearm_size').verbose_name
        self.assertEquals(field_label, 'left forearm size')

    def test_right_forearm_size_label(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_label = measurement._meta.get_field('right_forearm_size').verbose_name
        self.assertEquals(field_label, 'right forearm size')

    def test_left_thigh_size_label(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_label = measurement._meta.get_field('left_thigh_size').verbose_name
        self.assertEquals(field_label, 'left thigh size')

    def test_right_thigh_size_label(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_label = measurement._meta.get_field('right_thigh_size').verbose_name
        self.assertEquals(field_label, 'right thigh size')

    def test_left_calf_size_label(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_label = measurement._meta.get_field('left_calf_size').verbose_name
        self.assertEquals(field_label, 'left calf size')

    def test_right_calf_size_label(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_label = measurement._meta.get_field('right_calf_size').verbose_name
        self.assertEquals(field_label, 'right calf size')

    def test_object_name_is_date_user(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        expected_object_name = f'{measurement.date} {measurement.user.username}'
        self.assertEquals(expected_object_name, str(measurement))

# test for BodyCircumferenceMeasurements model max_digits and decimal_places

    def test_neck_size_options(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_options = measurement._meta.get_field('neck_size')
        self.assertEquals(field_options.max_digits, 6)
        self.assertEquals(field_options.decimal_places, 2)

    def test_chest_size_options(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_options = measurement._meta.get_field('chest_size')
        self.assertEquals(field_options.max_digits, 6)
        self.assertEquals(field_options.decimal_places, 2)

    def test_waist_size_options(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_options = measurement._meta.get_field('waist_size')
        self.assertEquals(field_options.max_digits, 6)
        self.assertEquals(field_options.decimal_places, 2)

    def test_left_bicep_size_options(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_options = measurement._meta.get_field('left_bicep_size')
        self.assertEquals(field_options.max_digits, 6)
        self.assertEquals(field_options.decimal_places, 2)

    def test_right_bicep_size_options(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_options = measurement._meta.get_field('right_bicep_size')
        self.assertEquals(field_options.max_digits, 6)
        self.assertEquals(field_options.decimal_places, 2)

    def test_left_forearm_size_options(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_options = measurement._meta.get_field('left_forearm_size')
        self.assertEquals(field_options.max_digits, 6)
        self.assertEquals(field_options.decimal_places, 2)

    def test_right_forearm_size_options(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_options = measurement._meta.get_field('right_forearm_size')
        self.assertEquals(field_options.max_digits, 6)
        self.assertEquals(field_options.decimal_places, 2)

    def test_left_thigh_size_options(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_options = measurement._meta.get_field('left_thigh_size')
        self.assertEquals(field_options.max_digits, 6)
        self.assertEquals(field_options.decimal_places, 2)

    def test_right_thigh_size_options(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_options = measurement._meta.get_field('right_thigh_size')
        self.assertEquals(field_options.max_digits, 6)
        self.assertEquals(field_options.decimal_places, 2)

    def test_left_calf_size_options(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_options = measurement._meta.get_field('left_calf_size')
        self.assertEquals(field_options.max_digits, 6)
        self.assertEquals(field_options.decimal_places, 2)

    def test_right_calf_size_options(self):
        measurement = BodyCircumferenceMeasurements.objects.get(id=1)
        field_options = measurement._meta.get_field('left_calf_size')
        self.assertEquals(field_options.max_digits, 6)
        self.assertEquals(field_options.decimal_places, 2)

# test for BodyCircumferenceMeasurements data is retrieved correctly from database and saved to database

    def test_save_and_retrieve(self):
        user = get_user_model().objects.create_user(username='testuser2', password='12345')
        BodyCircumferenceMeasurements.objects.create(
            user=user,
            neck_size=12.00,
            chest_size=34.00,
            waist_size=28.00,
            left_bicep_size=11.00,
            right_bicep_size=11.00,
            left_forearm_size=10.00,
            right_forearm_size=10.00,
            left_thigh_size=22.00,
            right_thigh_size=22.00,
            left_calf_size=15.00,
            right_calf_size=15.00
    )
        saved_measurement = BodyCircumferenceMeasurements.objects.get(user=user)
        self.assertEquals(saved_measurement.neck_size, Decimal('12.00'))
        self.assertEquals(saved_measurement.chest_size, Decimal('34.00'))
        self.assertEquals(saved_measurement.waist_size, Decimal('28.00'))
        self.assertEquals(saved_measurement.left_bicep_size, Decimal('11.00'))
        self.assertEquals(saved_measurement.right_bicep_size, Decimal('11.00'))
        self.assertEquals(saved_measurement.left_forearm_size, Decimal('10.00'))
        self.assertEquals(saved_measurement.right_forearm_size, Decimal('10.00'))
        self.assertEquals(saved_measurement.left_thigh_size, Decimal('22.00'))
        self.assertEquals(saved_measurement.right_thigh_size, Decimal('22.00'))
        self.assertEquals(saved_measurement.left_calf_size, Decimal('15.00'))
        self.assertEquals(saved_measurement.right_calf_size, Decimal('15.00'))

    # test for BodyCircumferenceMeasurements data is deleted correctly from database

    def test_user_deletion(self):
        user = get_user_model().objects.create_user(username='testuser2', password='12345')
        BodyCircumferenceMeasurements.objects.create(
            user=user,
            neck_size=12.00,
            chest_size=34.00,
            waist_size=28.00,
            left_bicep_size=11.00,
            right_bicep_size=11.00,
            left_forearm_size=10.00,
            right_forearm_size=10.00,
            left_thigh_size=22.00,
            right_thigh_size=22.00,
            left_calf_size=15.00,
            right_calf_size=15.00
        )

        user_id = user.id
        user.delete()

        with self.assertRaises(get_user_model().DoesNotExist):
            get_user_model().objects.get(id=user_id)

        self.assertFalse(BodyCircumferenceMeasurements.objects.filter(user_id=user_id).exists())
