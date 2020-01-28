from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to ='images')

    def __str__(self):
        return self.title

class Dosya(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
