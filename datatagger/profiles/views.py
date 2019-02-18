from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from profiles.models import Project
from .forms import RegisterForm
# Create your views here.

def index(request):
    # View code here...
    return render(request, 'index.html')

class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = 'index'
    success_message = "Your account was created successfully. Please check your email."

    def dispatch(self, *args, **kwargs):
        # if self.request.user.is_authenticated():
        #     return redirect("/logout")
        return super(RegisterView, self).dispatch(*args, **kwargs)

class ProjectListView( ListView):
    def get_queryset(self):
        # return Product.objects.filter(owner=self.request.user)
        return Project.objects.all()