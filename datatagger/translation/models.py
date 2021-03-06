from django.db import models
from profiles.models import Profile, Project, LanguageText
from django.db.models.signals import post_save


def default_user():
    try:
        comment = Profile.objects.get(pk=1).pk
    except:
        comment = None
    return comment


class TranslateOrigin(models.Model):
    text             = models.CharField( max_length=500, unique=True)
    language         = models.ForeignKey(LanguageText, on_delete=models.PROTECT)
    timestamp        = models.DateTimeField(auto_now_add=True)
    project_name     = models.ForeignKey(Project, on_delete=models.PROTECT)
    can_be_tagged    = models.BooleanField(default=False)
    validated        = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class PartiallyTranslated(models.Model):
    language                    = models.ForeignKey(LanguageText, on_delete=models.PROTECT)
    partially_translated_text   = models.CharField(max_length=500) 
    origin_text                 = models.ForeignKey(TranslateOrigin, on_delete=models.CASCADE)
    project_name                = models.ForeignKey(Project, on_delete=models.PROTECT)
    timestamp                   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.language) + ' __ ' +self.partially_translated_text

class TranslatedText(models.Model):

    language                     = models.ForeignKey(LanguageText, on_delete= models.PROTECT)
    translated_text              = models.CharField(max_length=500)
    tagged_by                    = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    partially_correct_text       = models.ForeignKey(PartiallyTranslated, on_delete=models.SET_NULL, blank=True, null=True)
    origin_text                  = models.ForeignKey(TranslateOrigin, on_delete=models.CASCADE, related_name="origin")
    timestamp                    = models.DateTimeField(auto_now_add=True)
    updated                      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.language) + ' __ ' +self.translated_text




