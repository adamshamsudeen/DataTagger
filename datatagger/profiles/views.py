from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

def index(request):
    # View code here...
    return render(request, 'index.html')



# class ProductListView( ListView):
#     def get_queryset(self):
#         # return Product.objects.filter(owner=self.request.user)
#         return Projects.objects.all()