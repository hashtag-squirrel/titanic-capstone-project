from django import forms
from predictor.models import UserModel

class UserForm(forms.ModelForm):

     gender = forms.ChoiceField(choices=[('', 'select')] + UserModel.gender_choices,required=False)
     travel_class=forms.ChoiceField(choices=[('', 'select')] + UserModel.travel_class_choices,required=False)
     port_of_embarkation=forms.ChoiceField(choices=[('', 'select')] + UserModel.embarkation_choices,required=False)

     class Meta():
        model=UserModel
        fields=('full_name','age','gender','travel_class','port_of_embarkation','cabin')
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter full name','class': 'form-control'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Enter age','class': 'form-control'}),   
            'cabin': forms.TextInput(attrs={'class': 'form-control'}),          
        }

        

