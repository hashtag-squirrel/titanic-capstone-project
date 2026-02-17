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
                'min':1,
                'max':100,
                'class': 'form-control'}),
            'is_alone': forms.CheckboxInput(),
            'with_parents': forms.CheckboxInput(),
            'with_spouse': forms.CheckboxInput(),
            'with_children': forms.CheckboxInput(),
            'with_siblings':forms.CheckboxInput(),
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

   
    def clean(self):
        cleaned_data = super().clean()

        is_alone = cleaned_data.get("is_alone")
        with_parents = cleaned_data.get("with_parents")
        with_spouse = cleaned_data.get("with_spouse")
        with_children = cleaned_data.get("with_children")
        with_siblings = cleaned_data.get("with_siblings")

       
        if not (is_alone or with_parents or with_spouse or with_children or with_siblings):
            raise forms.ValidationError(
                "Please select at least one option from travelled."
            )

        return cleaned_data


