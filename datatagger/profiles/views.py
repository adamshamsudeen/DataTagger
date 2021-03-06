from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from profiles.models import Project, Profile
from .forms import RegisterForm, ProfileForm

# Create your views here.


def index(request):
    # View code here...
    return render(request, 'new.html')


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')
    success_message = "Your account was created successfully. Please check your email."

    def dispatch(self, *args, **kwargs):
        # if self.request.user.is_authenticated():
        #     return redirect("/logout")
        return super(RegisterView, self).dispatch(*args, **kwargs)


class ProjectList(ListView):
    # def get_queryset(self):
        # return Product.objects.filter(owner=self.request.user)
    model =  Project


@login_required()
def profile_view(request):
    # if request.user.is_authenticated:
    # form = ProfileForm
    # instance = User.get_object_or_404(Profile, id=id)
    form = ProfileForm(request.POST or None, instance=request.user.profile)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/profile/')
    return render(request, 'profile.html', {'form': form})
