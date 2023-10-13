

from django import forms
from students.models import Student


class StudentForm(forms.Form):
    name = forms.CharField(required=True, label='Student Name')
    email = forms.EmailField()
    grade = forms.IntegerField(required=True)
    image = forms.ImageField()
    gender = forms.ChoiceField(
        choices=[('m', 'Male'), ('f', 'Female')])

    # define your own validation rules
    # email unique
    def clean_email(self):
        emailfound = Student.objects.filter(email=self.cleaned_data['email']).exists()
        if emailfound:
            raise forms.ValidationError('Email already registered before')

        return self.cleaned_data['email']