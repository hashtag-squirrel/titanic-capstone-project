from django.shortcuts import render
from predictor.forms import UserForm

# Create your views here.
def userforminfo(request):
   user_form=UserForm(data=request.POST)
   return render(request,'predictor/userform.html',
                 {'user_form':user_form})