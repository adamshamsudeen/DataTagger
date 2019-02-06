from django.db import models

# Create your models here.
class TranlateOrigin(models.Model):
    text         = models.CharField( max_length=500)
    language     = models.CharField(max_length=50)