from django.shortcuts import render

# Create your views here.

def index(request):
    # View code here...
    return render(request, 'index.html')