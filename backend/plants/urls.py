from django.urls import path
from . import views

urlpatterns = [
    path('plants/<int:pk>/', views.plant_detail, name='plant_detail'),
]
