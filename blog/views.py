from unittest import result
from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog(request):
    blog = Blog.objects.all()
    context = {'blog' : blog}
    return render(request, 'index.html', context)

def blogPost(request, slug):
    post = Blog.objects.filter(slug=slug)
    context = {'post' : post}
    print(context)
    return render(request, 'blog.html', context)


