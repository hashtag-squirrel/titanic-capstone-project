from django.test import TestCase
from django.urls import reverse
from .models import UserModel, PredictionModel
from .forms import UserForm

# Create your tests here.

# Test creating a Usermodel
class UserModelTest(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create(
            title='mr',
            full_name='John Doe',
            age=30,
            gender='0',
            travel_class='1',
            is_alone=True
        )

    def test_user_creation(self):
        self.assertEqual(self.user.full_name, 'John Doe')
        self.assertEqual(self.user.age, 30)
        self.assertEqual(self.user.gender, '0')

# Test creating a PreditionModel
class PredictionModelTest(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create(
            title='mrs',
            full_name='Jane Doe',
            age=28,
            gender='1',
            travel_class='2'
        )

        self.prediction = PredictionModel.objects.create(
            input_data=self.user,
            result=1,
            probability="0.82"
        )

    def test_prediction_creation(self):
        self.assertEqual(self.prediction.result, 1)
        self.assertEqual(self.prediction.probability, "0.82")
