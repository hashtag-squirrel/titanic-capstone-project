from django.urls import path,re_path,include
from predictor import views

app_name='predictor'

urlpatterns = [
   
     path(r'^userform/', views.userforminfo, name='userforminfo'),
]