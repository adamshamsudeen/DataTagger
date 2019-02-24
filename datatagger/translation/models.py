from django.db import models
from profiles.models import Profile, Project, LanguageText
from django.db.models.signals import post_save


def default_user():
    return Profile.objects.get(pk=1).pk


class TranslateOrigin(models.Model):
    text             = models.CharField( max_length=500)
    language         = models.ForeignKey(LanguageText, on_delete= models.PROTECT)
    timestamp        = models.DateTimeField(auto_now_add=True)
    project_name     = models.ForeignKey(Project, on_delete=models.PROTECT)

    def __str__(self):
        return self.text

class PartiallyTranslated(models.Model):
    language                    = models.ForeignKey(LanguageText, on_delete= models.PROTECT)
    partially_translated_text   = models.CharField(max_length=500) 
    origin_text                 = models.ForeignKey(TranslateOrigin, on_delete= models.CASCADE)
    project_name                = models.ForeignKey(Project, on_delete=models.PROTECT)
    timestamp                   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.language) + ' __ ' +self.partially_translated_text

class TranslatedText(models.Model):

    language                     = models.ForeignKey(LanguageText, on_delete= models.PROTECT)
    translated_text              = models.CharField(max_length=500)
    tagged_by                    = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default=default_user)
    partially_correct_text       = models.ForeignKey(PartiallyTranslated, on_delete=models.SET_NULL, blank=True, null=True)
    origin_text                  = models.ForeignKey(TranslateOrigin, on_delete=models.CASCADE, related_name="origin")
    timestamp                    = models.DateTimeField(auto_now_add=True)
    updated                      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.language) + ' __ ' +self.translated_text




def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        
        profile, is_created = Profile.objects.get_or_create(user=instance)
        # default_user_profile = Profile.objects.get_or_create(user__id=1)[0] #user__username=
        # default_user_profile.followers.add(instance)
        #profile.followers.add(default_user_profile.user)
        #profile.followers.add(2)

post_save.connect(post_save_user_receiver, sender=TranslatedText)