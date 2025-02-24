from django import forms 
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth.models import User,Permission,Group
import re
from tasks.forms import StyleFormMixin
from django import forms
from django.contrib.auth.models import User


# code code code code code 

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
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "w-full p-2 border rounded-lg", "placeholder": "Enter Password"})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "w-full p-2 border rounded-lg", "placeholder": "Confirm Password"})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
        widgets = {
            "username": forms.TextInput(attrs={"class": "w-full p-2 border rounded-lg", "placeholder": "Enter Username"}),
            "first_name": forms.TextInput(attrs={"class": "w-full p-2 border rounded-lg", "placeholder": "Enter First Name"}),
            "last_name": forms.TextInput(attrs={"class": "w-full p-2 border rounded-lg", "placeholder": "Enter Last Name"}),
            "email": forms.EmailInput(attrs={"class": "w-full p-2 border rounded-lg", "placeholder": "Enter Email"}),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        error = []

        if not re.search(r'[@#$%^&+=]', password):
            error.append('Password must have at least one special character (@#$%^&+=)')
        if not re.search(r'[A-Z]', password):
            error.append('Password must contain at least one uppercase letter (A-Z).')
        if not re.search(r'[a-z]', password):
            error.append('Password must contain at least one lowercase letter (a-z).')
        if not re.search(r'[0-9]', password):
            error.append('Password must contain at least one number (0-9).')
        if len(password) < 8:
            error.append('Password must be at least 8 characters long.')

        if password != confirm_password:
            error.append('Passwords do not match.')

        if error:
            raise forms.ValidationError(error)

        return password


class CustomLoginForm(StyleFormMixin,AuthenticationForm):
    def __init__(self , *args , **kwargs):
        super().__init__(*args , **kwargs)

class AssignedRoleForm(StyleFormMixin , forms.Form):
    Role = forms.ModelChoiceField(
        queryset= Group.objects.all(),
        empty_label="select a role "
    )

class CreateGroupForm(StyleFormMixin , forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required = False,
        label = 'Assign Permission'
    )

    class Meta:
        model = Group
        fields = ['name','permissions']