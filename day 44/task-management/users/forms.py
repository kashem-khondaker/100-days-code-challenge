from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name' ,'email', 'password1' , 'password2']
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm , self).__init__(*args, **kwargs)

        # self.fields['username'].help_text = None
        for fieldname  in ['username' , 'password1' , 'password2']:
            self.fields[fieldname].help_text = None

class CustomRegistrationForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.TextInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username' , 'first_name' , 'last_name' , 'email' , 'password' , 'confirm_password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        error = []

        # if len(password)< 8 or len(confirm_password) < 8:
        #     print('Password must be 8 character long')

        #     raise forms.ValidationError('Password must be at least 8 character long ')
        # return password
        if not re.search(r'[@#$%^&+=]', password):  # Ensure at least one special character
            error.append('Password must have one special character ')
        if not re.search(r'[A-Z]' , password):  # Ensure at least one special character
            error.append('Password must A-Z.')
        
        if not re.search(r'[a-z]', password):  # Ensure at least one special character
            error.append('Password must a-z.')
        if not re.search(r'[0-9]', password):  # Ensure at least one special character
            error.append('Password must 0-9.')
        
        if len(password) < 8:  # Ensure minimum length of 8
            error.append('Password must be at least 8 characters long.')

        if error:
            raise forms.ValidationError(error)
        
        return password

        # if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
        #     raise forms.ValidationError('password must have special character')
    
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            print('Password not matched !')
            raise forms.ValidationError('Password not matched ! ')
        return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_exists = User.objects.filter(email=email).exists()

        if email_exists:
            raise forms.ValidationError('Email already exists')
        return email