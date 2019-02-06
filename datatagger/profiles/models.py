from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.
class Profile(models.Model):
    user              = models.OneToOneField(User, on_delete=models.CASCADE) # user.profile
    # followers         = models.ManyToManyField(User, related_name='is_following', blank=True) # user.is_following.all()
    #following         = models.ManyToManyField(User, related_name='following', blank=True) # user.following.all()
    profession        = models.CharField(max_length=120, blank=True, null=True)
    activated         = models.BooleanField(default=True)
    timestamp         = models.DateTimeField(auto_now_add=True)
    updated           = models.DateTimeField(auto_now=True)
    contributions     = models.IntegerField()


    def __str__(self):
        return self.user.username