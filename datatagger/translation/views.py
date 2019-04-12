from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import TranslateOrigin, TranslatedText
from django import forms
from profiles.models import LanguageText
from .forms import TranslateForm


def _get_translate_object(language):
    # approach1
    # to_translate = TranslateOrigin.objects.filter(language=language)
    # to_translate = to_translate.order_by('?').first()

    # approach2
    # get a record from translateorigin which has no record in translatedtext
    to_translate = TranslateOrigin.objects.filter(
        origin__isnull=True, language=language, can_be_tagged=True)
    return to_translate.order_by('?').first()


def translate(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TranslateForm(request.POST)
            if form.is_valid():
                text = form.cleaned_data['translated_text']
                language = form.cleaned_data['language']
                print(form.cleaned_data['origin'])
                orig_pk = form.cleaned_data['origin']
                print(text, language)
                language, _ = LanguageText.objects.get_or_create(
                    language=language)
                translation = TranslatedText(language=language, translated_text=text,
                                             tagged_by=request.user.profile,
                                             origin_text=TranslateOrigin.objects.get(
                                                 pk=orig_pk),
                                             )
                translation.save()
                form = TranslateForm()

        else:
            form = TranslateForm()
        chosen = True
        user_languages = request.user.profile.language.values_list(
            'language', flat=True)
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
        form = TranslateForm()

    if not chosen:
        to_translate = TranslateOrigin.objects.last()
    else:
        to_translate = _get_translate_object(language)
    context = {'origin': to_translate, 'form': form, 'profile_filled': chosen}
    return render(request, 'translate.html', context=context)



@staff_member_required
def validate_data(request):
    def get_lang():
        user_languages = request.user.profile.language.values_list(
            'language', flat=True)
        if 'ml' in user_languages:
            print("ml - user")
            language = LanguageText.objects.get(language='ml')

        elif 'ta' in user_languages:
            print("ta - user")
            language = LanguageText.objects.get(language='ta')
        else:
            language = LanguageText.objects.get(language='ta')
        return language

    if request.method == 'POST':
        if 'good_text' in request.POST:
            print("good")
            to_change = TranslateOrigin.objects.get(pk=request.POST.get("origin"))
            to_change.validated = True
            to_change.can_be_tagged = True
            to_change.save()
        elif 'bad_text' in request.POST:
            print("bad")
            to_change = TranslateOrigin.objects.get(pk=request.POST.get("origin"))
            to_change.validated = True
            to_change.save()
        

    lang = get_lang()
    print(lang)
    to_validate =  TranslateOrigin.objects.filter(language=lang, validated=False).order_by('?').first()
    context = {'origin': to_validate}
    return render(request, 'validate_translate.html', context=context)



