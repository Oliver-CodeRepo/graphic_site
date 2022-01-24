from django.shortcuts import render
from django.template import context

from base.models import Video

# Create your views here.

def index(request):
    v = Video.objects.all()
    context = {'v':v}
    return render(request, 'base/index.html', context)


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