from django.shortcuts import render
from django.template import context

from base.models import Video

# Create your views here.

def index(request):
    return render(request, 'base/index.html')

def videoView(request):
    v = Video.objects.all()
    context = {'v':v}
    return render(request, 'base/video.html', context)


def videoDetailView(request, slug):
    v = Video.objects.filter(slug=slug).first()
    context = {'v':v}
    return render(request, 'base/video_details.html', context)

def workView(request):
    context = {}
    return render(request, 'base/works.html', context)


def clientView(request):
    context = {}
    return render(request, 'base/clients.html', context)

def contactView(request):
    context = {}
    return render(request, 'base/contact.html', context)

def aboutView(request):
    context = {}
    return render(request, 'base/about.html', context)