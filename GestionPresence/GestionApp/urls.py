from django.urls import path
from . import views

urlpatterns = [
    path('list_employer/', views.list_employer, name='list_employer'), 
    
     
    
]