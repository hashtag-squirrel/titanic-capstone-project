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

