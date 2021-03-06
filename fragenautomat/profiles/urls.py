from django.contrib.auth import views as auth_views
from django.urls import path

from profiles import views


app_name = 'profiles'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='profiles/registration/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='profiles/registration/logout.html'
    ), name='logout'),
    path('register/', views.RegistrationView.as_view(), name='registration'),
    path('activation/', views.ActivationView.as_view(), name='activation'),

    path('<slug:username>/', views.ProfileView.as_view(), name='profile'),
]
