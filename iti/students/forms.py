

from django import forms
from students.models import Student
from tracks.models import Track

class StudentForm(forms.Form):
    name = forms.CharField(required=True, label='Student Name')
    email = forms.EmailField()
    grade = forms.IntegerField(required=True)
    image = forms.ImageField()
    gender = forms.ChoiceField(
        choices=[('m', 'Male'), ('f', 'Female')])
    track  =  forms.ModelChoiceField(
        Track.objects.all(), label='Track'
    )

    # define your own validation rules
    # email unique
    def clean_email(self):
        emailfound = Student.objects.filter(email=self.cleaned_data['email']).exists()
        if emailfound:
            raise forms.ValidationError('Email already registered before')

        return self.cleaned_data['email']