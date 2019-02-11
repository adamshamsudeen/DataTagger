from django.shortcuts import render
from django.views.generic import ListView
from models import Project
# Create your views here.

def index(request):
    # View code here...
    return render(request, 'index.html')



class ProjectListView( ListView):
    def get_queryset(self):
        # return Product.objects.filter(owner=self.request.user)
        return Project.objects.all()