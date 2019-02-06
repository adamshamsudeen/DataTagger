from django.db import models
from profiles.models import Profile



def default_user():
        return Profile.objects.get(pk=1).pk

class Project(models.Model):
    project_name      = models.CharField(max_length=120, unique=True)
    project_owner     = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default=default_user)
    timestamp         = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name

class TranslateOrigin(models.Model):
    text             = models.CharField( max_length=500)
    language         = models.CharField(max_length=2, default="en")
    timestamp        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text



class PartiallyTranslated(models.Model):
    language                    = models.CharField(max_length=2)
    partially_translated_text   = models.CharField(max_length=500) 
    origin_text                 = models.ForeignKey(TranslateOrigin, on_delete= models.CASCADE)
    project_name                = models.ForeignKey(Project, on_delete=models.PROTECT)
    timestamp                   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.language + ' ' +self.partially_translated_text

class TranslatedText(models.Model):
    language                    = models.CharField(max_length=2)
    translated_text              = models.CharField(max_length=500)
    tagged_by                    = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default=default_user)
    partially_correct_text       = models.ForeignKey(PartiallyTranslated, on_delete=models.SET_NULL, blank=True, null=True)
    origin_text                  = models.ForeignKey(TranslateOrigin, on_delete=models.CASCADE)
    project_name                 = models.ForeignKey(Project, on_delete=models.PROTECT)
    timestamp                    = models.DateTimeField(auto_now_add=True)
    updated                      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.language + ' ' +self.translated_text



