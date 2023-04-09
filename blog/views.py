from unittest import result
from django.shortcuts import render
from .models import Blog
import sys
sys.path.append("..")
from home.models import Newsletter

# Create your views here.
def blogPost(request, slug):
    if request.method == "POST":
        email = request.POST['nwseml']
        newsletter = Newsletter(email=email)
        newsletter.save()
    post = Blog.objects.filter(slug=slug)
    context = {'post' : post}
    return render(request, 'blog.html', context)


