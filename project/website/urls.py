# website/urls.py  
from django.urls import path  
from . import views  

urlpatterns = [  
    path('', views.home, name='home'),  # Home page of the website  
    # Add more URL patterns here as needed  
]