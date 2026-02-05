from django.shortcuts import render

# Create your views here.
def userform(request):
    return render(request,'predictor/userform.html')
