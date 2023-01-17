from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Post, Tag 
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def homepage(request):
    posts=Post.objects.filter(featured=True,active=True)[0:3]
    context={'posts':posts}
    return render(request, 'index.html', context)

class PostView(generic.DetailView):
    template_name='post.html'
    
    def get_queryset(self):
        queryset=Post.objects.all()
        return queryset


def posts(request):
    posts=Post.objects.filter(active=True)
    context={'posts':posts}
    return render(request, 'posts.html', context)


# def profile(request):
#     return render (request, 'profile.html')


def sendEmail(request):

    if request.method == 'POST':

        template=render_to_string('email_template.html', {
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })

        email=EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['sarvarusmn@gmail.com']
            )

        email.fail_silently=False
        email.send()
    return render(request, 'email_sent.html')
  