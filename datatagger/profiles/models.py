from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
# from translation.models import LanguageText
User = settings.AUTH_USER_MODEL


class LanguageText(models.Model):
    language         = models.CharField(max_length=2)

    def __str__(self):
        return self.language


class Profile(models.Model):
    user              = models.OneToOneField(User, on_delete=models.CASCADE) # user.profile
    profession        = models.CharField(max_length=120, blank=True, null=True)
    activated         = models.BooleanField(default=True)
    timestamp         = models.DateTimeField(auto_now_add=True)
    updated           = models.DateTimeField(auto_now=True)
    contributions     = models.IntegerField(default='0')
    language          = models.ManyToManyField(LanguageText,
                         related_name='all_the_languages', blank=True)
    full_name         = models.CharField(max_length=120, blank=True, null=True)
    dialect           = models.CharField(max_length=120, blank=True, null=True)
    mother_tongue     = models.ForeignKey(LanguageText, related_name='mother_tongue',
                                 on_delete= models.PROTECT, blank=True, null = True)


    def __str__(self):
        return self.user.username
        
    def send_activation_email(self):
        if True:#not self.activated:
            # self.activation_key = code_generator()# 'somekey' #gen key
            self.save()
            #path_ = reverse()
            # path_ = reverse('activate', kwargs={"code": self.activation_key})
            # full_path = "https://startuplog.co/" + path_
            # subject = 'Activate Account'
            # from_email = settings.DEFAULT_FROM_EMAIL
            # message = f'Activate your account here: {full_path}'
            # recipient_list = [self.user.email]
            # html_message = f'<p>Activate your account here: <a href="{full_path}">Activate Email</a></p>'
            # print(html_message)
            # sent_mail = send_mail(
            #                 subject, 
            #                 message, 
            #                 from_email, 
            #                 recipient_list, 
            #                 fail_silently=False, 
            #                 html_message=html_message)
            # # print(sent_mail)
            # sent_mail = False
            return #sent_mail

def default_user():
    return Profile.objects.get(pk=1).pk

class Project(models.Model):
    project_name      = models.CharField(max_length=120, unique=True)
    project_owner     = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default=default_user)
    timestamp         = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        # default_user_profile = Profile.objects.get_or_create(user__id=1)[0] #user__username=
        # default_user_profile.followers.add(instance)
        #profile.followers.add(default_user_profile.user)
        #profile.followers.add(2)

post_save.connect(post_save_user_receiver, sender=User)