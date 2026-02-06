from django import forms
from predictor.models import UserModel

class UserForm(forms.ModelForm):
     class Meta():
        model=UserModel
        fields=('full_name','age','gender')
