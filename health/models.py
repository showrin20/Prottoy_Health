from django.db import models

# Create your models here.
class UserHealth(models.Model):
    isSmoke = models.BooleanField(blank=True,null=True)
    isDiabetes = models.BooleanField(blank=True,null=True)
    isFever = models.BooleanField(blank=True,null=True)
    diseaseImage = models.ImageField(blank=True,upload_to='images/', null=True)
