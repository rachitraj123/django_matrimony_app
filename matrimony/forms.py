from django import forms

from .models import *
from django.core.validators import *
from django.core.exceptions import *


def email_validator(email):
    if email.split('@')[1].split(".")[0].lower()=="hotmail":
        raise ValidationError("Invalid email found....")
    else:
        pass


class contactform(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(validators=[EmailValidator(),email_validator])
    verifyemail = forms.CharField(validators=[EmailValidator(),email_validator])
    message = forms.CharField(widget=forms.Textarea())
    
    
    def clean(self):
        cleaned_data = super().clean()
        
        name = cleaned_data['name']
        cleaned_data['email'] = cleaned_data['email'].lower()
        cleaned_data['verifyemail'] = cleaned_data['verifyemail'].lower()
        message = cleaned_data['message']
        
        if cleaned_data['email'] != cleaned_data['verifyemail']:
            raise forms.ValidationError('Email not matched......')
        else:
            pass
        
class new_profile_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
    