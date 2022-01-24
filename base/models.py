from django.db import models
from  embed_video.fields  import  EmbedVideoField

# Create your models here.
class Video(models.Model):
    """ video model """
    title = models.CharField(max_length=200)
    video = EmbedVideoField()
    
    def __str__(self):
        return self.title if self.title else 'video_{}'.format(self.id)
    
    class Meta:
        verbose_name_plural = 'Videos'