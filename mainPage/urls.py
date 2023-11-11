from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.group, name='group'),
    path('login/', views.LoginPage, name='login'),
    path('signup/',views.SignupPage, name='signup'),
    path('logout/',views.LogoutPage, name='logout'),
    path('about', views.about, name="about"),
]