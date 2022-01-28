from django.db import models
from  embed_video.fields  import  EmbedVideoField
import string
import random

# from django.utils.text import slugify


# def rand_slug():
#     return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))



# Create your models here.
class Video(models.Model):
    """ video model """
    title = models.CharField(max_length=200)
    video = EmbedVideoField()
    details = models.TextField()
        
    def __str__(self):
        return self.title if self.title else 'video_{}'.format(self.id)
    
    class Meta:
        verbose_name_plural = 'Videos'