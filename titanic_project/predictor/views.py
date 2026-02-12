from django.shortcuts import render, redirect
from django.urls import reverse
from predictor.forms import UserForm
from predictor.utils import predict


def home(request):
    return render(request, "predictor/index.html")


# Create your views here.
def userforminfo(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            data = request.POST
            prediction_output,prob_value = predict(data, user)

            return render(request, 'predictor/results.html', {
                'result': prediction_output,
                'probability': prob_value,
                'user': user
            })

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'predictor/userform.html', {'user_form': user_form})


def history_page(request):
    return render(request, 'predictor/history-page.html')
