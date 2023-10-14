

from django import  forms
from tracks.models import Track


class TrackModelForm(forms.ModelForm):
    # ask django to create form based on the model
    class Meta:
        # define the form architure
        model  = Track
        fields = '__all__'

    def clean_name(self):
        if self.cleaned_data['name'].lower() == 'track':
            raise forms.ValidationError("Track name shouldn't be Track")
        return self.cleaned_data['name']


