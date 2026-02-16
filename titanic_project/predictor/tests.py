from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
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

# # Test creating a PredictionModel
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

# Form test
class UserFormTest(TestCase):

    def test_valid_form(self):
        form_data = {
            "title": "mr",
            "full_name": "Test User",
            "age": 25,
            "gender": "0",
            "travel_class": "1",
            "is_alone": True,
        }

        form = UserForm(data=form_data)
        self.assertTrue(form.is_valid())


# View test
class ViewTest(TestCase):

    def test_homepage_loads(self):
        response = self.client.get(reverse("predictor:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "predictor/index.html")


    def test_userform_get_loads(self):
        response = self.client.get(reverse("predictor:userforminfo"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "predictor/userform.html")

    @patch("predictor.views.predict")
    def test_userform_post_valid(self, mock_predict):
        mock_predict.return_value = (1, "0.85")

        form_data = {
            "title": "mr",
            "full_name": "Test User",
            "age": 30,
            "gender": "0",
            "travel_class": "1",
            "is_alone": True,
        }

        response = self.client.post(
            reverse("predictor:userforminfo"),
            data=form_data
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "predictor/results.html")
        self.assertContains(response, "0.85")


# History page test
    def test_history_page_loads(self):
        response = self.client.get(reverse("predictor:history-page"))
        self.assertEqual(response.status_code, 200)


