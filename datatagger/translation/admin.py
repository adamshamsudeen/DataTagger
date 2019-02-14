from django.contrib import admin

# Register your models here.

from .models import (
            # Project,
            TranslateOrigin,
            PartiallyTranslated,
            TranslatedText
            )

# admin.site.register(Project)
admin.site.register(TranslateOrigin)
admin.site.register(TranslatedText)
admin.site.register(PartiallyTranslated)