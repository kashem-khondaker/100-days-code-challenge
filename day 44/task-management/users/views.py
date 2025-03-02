from django.shortcuts import render , redirect,HttpResponse
from django.contrib.auth.models import Group
from users.forms import  CustomRegistrationForm,AssignedRoleForm , CreateGroupForm,CustomPasswordChangeForm , CustomPasswordResetForm , CustomPasswordResetConfirmForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.forms import LoginForm , EditProfileForm
from users.models import CustomUser
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Prefetch
from django.contrib.auth.decorators import login_required , user_passes_test
from django.contrib.auth.views import LoginView , PasswordChangeView ,PasswordResetView , PasswordResetConfirmView
from django.views.generic import TemplateView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

# from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


User = get_user_model()

def sign_up(request):
    if request.method == "POST":
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            
            messages.success(request, f'Welcome {user.username}! A confirmation mail has been sent. Please check your email.')
            return redirect('sign-in')  
        else:
            print("Form errors:", form.errors)  # Errors দেখার জন্য

    else:
        form = CustomRegistrationForm()

    return render(request, 'registration/signUp.html', {'form': form})



def sign_in(request):

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request , user)
            return redirect('home')

    return render(request, 'registration/login.html' , {'form':form})


class CustomLoginView(LoginView):
    form_class = LoginForm

    def get_success_url(self):
        next_url = self.request.GET.get('next') or self.request.POST.get('next')
        return next_url if next_url else super().get_success_url()


class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['username'] = self.request.user.username
        context['email'] =  self.request.user.email
        context['name'] = self.request.user.get_full_name()
        context['bio'] = self.request.user.bio
        context['profile_image'] = self.request.user.profile_image

        context['member_since'] = self.request.user.date_joined
        context['last_login'] =  self.request.user.last_login

        return context
    
"""

class EditProfileView(UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'accounts/update_profile.html'
    context_object_name = 'form'

    def get_object(self):
        return self.request.user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['userprofile'] = UserProfile.objects.get(user=self.request.user)
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = UserProfile.objects.get(user=self.request.user)
        print("views", user_profile)
        context['form'] = self.form_class(
            instance=self.object, userprofile=user_profile)
        return context

    def form_valid(self, form):
        form.save(commit=True)
        return redirect('profile_view')

"""
    
class EditProfileView(UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'accounts/update_profile.html'
    context_object_name = 'form'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return redirect('profile_view')
    
class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'registration/reset_password.html'
    success_url = reverse_lazy('sign-in')
    html_email_template_name = 'registration/reset_email.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['protocol'] = 'https' if self.request.is_secure() else 'http'
        context['domain'] = self.request.get_host()
        print(context)
        return context

    def form_valid(self, form):
        messages.success(
            self.request, 'A Reset email sent. Please check your email')
        return super().form_valid(form)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomPasswordResetConfirmForm
    template_name = 'registration/reset_password.html'
    success_url = reverse_lazy('sign-in')

    def form_valid(self, form):
        messages.success(
            self.request, 'Password reset successfully')
        return super().form_valid(form)


@login_required
def user_logout(request):
    # print('something ')
    print(request.method)
    if request.method == "POST":
        # print('wellcome')
        logout(request)
        messages.success(request, "You have successfully logged out.")  # Logout success message
        return redirect('home')

    return redirect('home')

class ChangePassword(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    form_class = CustomPasswordChangeForm


def activate_user(request , user_id , token):
    try:
        user = User.objects.get(id = user_id)
        if default_token_generator.check_token(user , token):
            user.is_active = True
            user.save()

            return redirect('sign-in')
        else:
            return HttpResponse("Invalid id or token !")
    except User.DoesNotExist:
        return HttpResponse("User not found !")

# test for users

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

@user_passes_test(is_admin , login_url='no_permission')
def Admin_dashboard(request):

    users = User.objects.prefetch_related(
        Prefetch('groups' , queryset=Group.objects.all() , to_attr='all_groups')
        ).all()
    
    print(users)

    for user in users:
        if user.all_groups:
            user.group_name = user.all_groups[0].name
        else:
            user.group_name = 'No Group Assigned'
    return render(request , 'Admin/admin_dashboard.html' , {"users":users})


@user_passes_test(is_admin , login_url='no_permission')
def assigned_role(request, user_id):
    user = User.objects.get(id=user_id)
    form = AssignedRoleForm()
    if request.method == "POST":
        form = AssignedRoleForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data.get('Role')  # Ensure it matches the form field name
            user.groups.clear()  # Remove old roles
            user.groups.add(role)

            messages.success(request, f"{user.username} has been assigned to the '{role.name}' role")
            return redirect('Admin_dashboard')
    return render(request, 'Admin/assign_role.html', {"form": form, "user": user})


@user_passes_test(is_admin , login_url='no_permission')
def Create_Group(request ):
    form = CreateGroupForm()
    if request.method == "POST":
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            messages.success(request , f'Group {group.name} has been created successfully .')
            return redirect('create-group')

    return render(request , 'Admin/create_group.html' , {'form':form})   



@user_passes_test(is_admin, login_url='no-permission')
def group_list(request):
    groups = Group.objects.prefetch_related('permissions').all()
    return render(request, 'Admin/view_group.html', {'groups': groups})

