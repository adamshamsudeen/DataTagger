from django.contrib import admin

# Register your models here.

from .models import (
            # Project,
            TranslateOrigin,
            PartiallyTranslated,
            TranslatedText
            )

admin.site.register(TranslateOrigin)
admin.site.register(PartiallyTranslated)


class TranslatedTextAdmin(admin.ModelAdmin):
       raw_id_fields = ('partially_correct_text','origin_text',)

admin.site.register(TranslatedText, TranslatedTextAdmin)