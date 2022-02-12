from django.db import models
from  embed_video.fields  import  EmbedVideoField
import uuid
from ckeditor.fields import RichTextField

SITES = (
    ('Youtube','Youtube'),
    ('Vimeo','Vimeo'),
)

# Create your models here.
class Video(models.Model):
    """ video model """
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length=200)
    video_url = EmbedVideoField()
    site_name = models.CharField(max_length=50, choices=SITES)
    details = RichTextField(blank = True, null=True)
        
    def __str__(self):
        return self.title if self.title else 'video_{}'.format(self.id)
    
    class Meta:
        verbose_name_plural = 'Videos'
        


class CustomerMessage(models.Model):
    """ Messages model """
    
    email = models.EmailField()
    sender = models.CharField(max_length=100) 
    subject = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return 'From: {} on subject: {}'.format(str(self.email), self.subject)
    
    