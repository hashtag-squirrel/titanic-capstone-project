from django import forms
from predictor.models import UserModel


class UserForm(forms.ModelForm):

    title = forms.ChoiceField(
        choices=[('', 'select')] + UserModel.title_choices,
        required=False)
    gender = forms.ChoiceField(
        choices=[('', 'select')] + UserModel.gender_choices,
        required=False)
    travel_class = forms.ChoiceField(
        choices=[('', 'select')] + UserModel.travel_class_choices,
        required=False)
    port_of_embarkation = forms.ChoiceField(
        choices=[('', 'select')] + UserModel.embarkation_choices,
        required=False)

    class Meta():
        model = UserModel
        fields = (
            'title',
            'full_name',
            'age',
            'gender',
            'travel_class',
            'port_of_embarkation',
            'is_alone',
            'with_parents',
            'with_spouse',
            'with_children',
            'with_siblings')
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Enter full name',
                'class': 'form-control'}),
            'age': forms.NumberInput(attrs={
                'placeholder': 'Enter age',
                'class': 'form-control'}),
            'is_alone': forms.CheckboxInput(),
            'with_parents': forms.CheckboxInput(),
            'with_spouse': forms.CheckboxInput(),
            'with_children': forms.CheckboxInput(),
            'with_siblings': forms.CheckboxInput(), 

        }
