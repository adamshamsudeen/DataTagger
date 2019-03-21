from django.contrib import admin
from django.urls import path
from .views import translate, validate_data

urlpatterns = [
    path('', translate, name='translate'),
    path('validate/', validate_data, name='validate_text')
  
]
