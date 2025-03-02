from django.urls import path
from users.views import sign_up,sign_in,Admin_dashboard,assigned_role , user_logout,activate_user , Create_Group , ChangePassword ,group_list,CustomLoginView,ProfileView , CustomPasswordResetView,CustomPasswordResetConfirmView, EditProfileView
from django.contrib.auth.views import LogoutView , PasswordChangeView , PasswordChangeDoneView

urlpatterns = [
    path('sign-up/' , sign_up , name="sign-up"),
    # path('sign-in/' , sign_in , name='sign-in'),
    path('sign-in/' , CustomLoginView.as_view(template_name = 'registration/login.html') , name='sign-in'),
    # path('log-out/', user_logout, name='logout'),
    path('log-out/', LogoutView.as_view(), name='logout'),
    path('activate/<int:user_id>/<str:token>/' , activate_user),
    path('admin/dashboard/' , Admin_dashboard , name="Admin_dashboard"),
    path('admin/assigned-role/<int:user_id>/',assigned_role , name="assigned_role"),
    path('admin/create-group/' , Create_Group , name="create-group"),
    path('admin/group-list/',group_list , name='group_list'),
    path('profile/',ProfileView.as_view() , name='profile_view'),
    path('password-change/', ChangePassword.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(
    template_name='accounts/password_change_done.html'), name='password_change_done'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/confirm/<uidb64>/<token>/',CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('edit-profile/' , EditProfileView.as_view() , name='edit_profile'),
]
