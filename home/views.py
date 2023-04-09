from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, Newsletter
import sys
sys.path.append("..")
from blog.models import Blog

# Create your views here.

def home(request):
    allblog = Blog.objects.all()
    context = {'allblog':allblog}

    if request.method == "POST":
        email = request.POST['nwseml']
        newsletter = Newsletter(email=email)
        newsletter.save()

    return render(request, 'index.html', context)

def contact(request):
    if request.method == "POST":
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']

        contact = Contact(message=message, email=email, name=name)
        contact.save()

    return render(request, 'contact.html')


