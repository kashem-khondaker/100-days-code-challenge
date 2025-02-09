from django.shortcuts import render
from django.contrib.auth.models import User
from users.forms import RegistrationForm
# Create your views here.

def Sign_Up(request):
    if request.method == "GET":
        form = RegistrationForm()
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # print(form.changed_data)
            # form.save()
            UserName = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # confirm_password = form.cleaned_data.get('password2')
            # if password == confirm_password:
            #     user = User.objects.create_user(username = UserName ,password = confirm_password)
            # else:
            #     print('password is not same ..')
            form.save()
            print(f'Welcome User {UserName}')
        else:
            print('form is not valid !')

    return render( request , 'registration/registration.html' , {'form':form} )
