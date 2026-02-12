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

    class Meta():
        model = UserModel
        fields = (
            'title',
            'full_name',
            'age',
            'gender',
            'travel_class',            
            'is_alone',
            'with_parents',
            'parents_count',
            'with_spouse',
            'spouse_count',
            'with_children',
            'children_count',
            'with_siblings',
            'siblings_count')
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
            'parents_count': forms.NumberInput(
                attrs={'class': 'count-input',
                       'min': 1,
                       'max':10,
                       'placeholder':'Specify count'}),

            'spouse_count': forms.NumberInput(
                attrs={'class': 'count-input',
                       'min': 1,
                       'max':10,
                       'placeholder':'Specify count'}),
            'children_count': forms.NumberInput(
                attrs={'class': 'count-input',
                       'min': 1,
                       'max':10,
                       'placeholder':'Specify count'}),

            'siblings_count': forms.NumberInput(
                attrs={'class': 'count-input',
                       'min': 1,
                       'max':10,
                       'placeholder':'Specify count'}),


        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["age"].required = True
        self.fields["gender"].required = True
        self.fields["travel_class"].required = True

