from django.shortcuts import render

# Create your views here.

def list_employer(request):
    
    return render(request, 'GestionApp/list_employees.html')
