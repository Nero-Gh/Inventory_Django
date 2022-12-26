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
]
