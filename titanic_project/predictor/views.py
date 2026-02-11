from django.shortcuts import render, redirect
from django.urls import reverse
from predictor.forms import UserForm
import joblib
import pandas as pd
from predictor.models import PredictionModel


def home(request):
    return render(request, "predictor/index.html")


# Create your views here.
def userforminfo(request):
    print('Test')
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            model = joblib.load('../ml_models/titanic_model.pkl')
            data = request.POST
            df = pd.DataFrame({
                'Pclass': int(data.get('travel_class')),
                'Sex': int(data.get('gender')),
                'Age': data.get('age')
            }, index=[0])

            test_df = pd.DataFrame({
                'Pclass': int(data.get('travel_class')),
                'Sex': int(data.get('gender')),
                'Age': data.get('age'),
                'SibSp': 1,
                'Parch': 0,
                'FamilySize': 1,
            }, index=[0])

            prediction = model.predict(test_df)
            probability = model.predict_proba(test_df)
            print(prediction)
            prediction = PredictionModel.objects.create(input_data=user, result=prediction[0], probability=probability)
            return redirect(reverse('predictor:home'))

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'predictor/userform.html', {'user_form': user_form})
