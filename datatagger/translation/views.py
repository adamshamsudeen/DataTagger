from django.shortcuts import render
from .models import TranslateOrigin
from django import forms
from .forms import TranslateForm
# Create your views here.


def translate(request):
    # View code here...
    tranlate_test = TranslateOrigin.objects.get()
    if request.method == 'POST':
        form = TranslateForm(request.POST)
        # print(request.json())
        if form.is_valid():
            text = form.cleaned_data['translated_text']
            language = form.cleaned_data['language']
            print(text, language)

    else:
        form = TranslateForm()
    return render(request, 'translate.html', context={'origin': tranlate_test, 'form':form})