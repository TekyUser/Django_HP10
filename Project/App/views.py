
from django.shortcuts import render

def index(request):
    return render(request, 'pages/home.html')

def contact(request):
    return render(request, 'pages/contact.html')

def error(request, exception):
    return render(request, 'pages/error.html', {'message': exception})
