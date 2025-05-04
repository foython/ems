from django.contrib import admin
from django.urls import path, include
from .views import SignUpView, LoginView, ProfileView

urlpatterns = [
    
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
    
]