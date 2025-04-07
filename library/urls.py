from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home_view, name='home'),  # Home page
    path('about/', views.about_view, name='about'),  # About page
    path('error/', views.error_view, name='error'),  # Simulate an error
]
