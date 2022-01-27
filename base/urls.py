from django.urls import path
from base.views import aboutView, clientView, contactView, index, videoDetailView, videoView, workView

app_name = 'base'

urlpatterns = [
    path('', index, name='index'),
    path('video', videoView, name='videos'),
    path('video/<int:id>', videoDetailView, name='video-details'),
    path('works', workView, name='works'),
    path('clients', clientView, name='clients'),
    path('about', aboutView, name='about'),
    path('contact', contactView, name='contact'),
]