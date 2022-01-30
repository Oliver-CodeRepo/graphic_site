from django.contrib import messages
from django.shortcuts import redirect, render
from base.forms import MessageForm
from base.globals import send_html_email

from base.models import Video

# Create your views here.

def index(request):
    return render(request, 'base/index.html')

def videoView(request):
    v = Video.objects.all()
    context = {'v':v}
    return render(request, 'base/video.html', context)


def videoDetailView(request, id):
    v = Video.objects.filter(id=id).first()
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

def send_message(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            to_list = form.cleaned_data['sender']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            
            email_context = {
                'to_list':to_list,
                'email': email,
                'subject':subject,
            }
            form.save()
            print('saved')
            send_mail = send_html_email([to_list, ], 'Message Reception Acknowledgement', 'emails/message.html', email_context )    
            print('message was sent', send_mail)        
            if send_mail:
                form.save()
                messages.info(request, 'Your concern/question was sent successfully, we will reach you as soon as possible')
                return redirect('base:contact')
            else:
                print('failed to send', send_mail, form.errors)
                return redirect('base:contact')
                
        else:
            print('failed', form.errors)
            return redirect('base:contact')
    
    
        