from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, Newsletter

# Create your views here.

def home(request):
    if request.method == "POST":
        email = request.POST['nwseml']

        newsletter = Newsletter(email=email)
        newsletter.save()

    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']

        contact = Contact(message=message, email=email, name=name)
        contact.save()

    return render(request, 'contact.html')


