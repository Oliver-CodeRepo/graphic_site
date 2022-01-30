from django.contrib import admin
from  embed_video.admin  import  AdminVideoMixin
from .models  import  CustomerMessage, Video

class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(Video, VideoAdmin)
admin.site.register(CustomerMessage)
# Register your models here.
