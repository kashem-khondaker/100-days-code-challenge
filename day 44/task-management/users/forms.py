from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name' ,'email', 'password1' , 'password2']
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm , self).__init__(*args, **kwargs)

        # self.fields['username'].help_text = None
        for fieldname  in ['username' , 'password1' , 'password2']:
            self.fields[fieldname].help_text = None
