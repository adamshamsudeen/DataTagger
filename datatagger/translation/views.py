from django.shortcuts import render
from .models import TranslateOrigin, TranslatedText
from django import forms
from profiles.models import LanguageText
from .forms import TranslateForm


def _get_translate_object(language):
    #approach1
    # to_translate = TranslateOrigin.objects.filter(language=language)
    # to_translate = to_translate.order_by('?').first()

    #approach2
    #get a record from translateorigin which has no record in translatedtext
    to_translate = TranslateOrigin.objects.filter(origin__isnull=True,language=language)
    return to_translate.order_by('?').first()

def translate(request):
    if request.user.is_authenticated:
        chosen = True
        user_languages = request.user.profile.language.values_list('language',flat=True)
        if 'ml' in user_languages:
            print("ml - user")
            language = LanguageText.objects.get(language='ml')
            
        elif 'ta' in user_languages:
            print("ta - user")
            language = LanguageText.objects.get(language='ta')
        else:
            chosen = False
    else:
        chosen = False

    if not chosen:
        to_translate = TranslateOrigin.objects.last()
    else:
        to_translate = _get_translate_object(language)

    if request.method == 'POST':
        form = TranslateForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['translated_text']
            language = form.cleaned_data['language']
            print(text, language)
            language, _ = LanguageText.objects.get_or_create(language=language)
            translation = TranslatedText(language=language,translated_text=text,
                        tagged_by = request.user.profile,
                        origin_text = to_translate,
                        )
            translation.save()


    else:
        form = TranslateForm()
    return render(request, 'translate.html', context={'origin': to_translate, 'form':form,'profile_filled':chosen})