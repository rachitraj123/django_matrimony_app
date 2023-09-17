from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import *

class RegistrationForm(UserCreationForm):
    
    gender = ChoiceField(choices=CustomUser.GENDER_CHOICES, widget=RadioSelect)
    
    class Meta:
        model = CustomUser
        fields = ['username','gender','email','password1','password2']