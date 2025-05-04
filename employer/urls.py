from django.urls import path
from .views import EmployerView, EmployerDetailView


urlpatterns = [
   
    path('employers/', EmployerView.as_view()),    
    path('employers/<int:pk>/', EmployerDetailView.as_view()),
    
]