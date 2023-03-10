from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('register/',views.register,name='user-register'),


    # login url
    path('', auth_view.LoginView.as_view(template_name='user/login.html'), name='user-login'),

    # logout url
    path('logout/', auth_view.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),

    #User Profile  
    path('profile', views.profile, name="user-profile"),


    #Edit Profile  
    path('profile/update', views.profile_update, name="user-profile-update"),


    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='user/password_reset.html'),name='password_reset'),
    path('password_reset_done/',auth_view.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_conmplete/',auth_view.PasswordResetCompleteView.as_view(),name='password_reset_complete')
]
