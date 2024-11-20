from django.shortcuts import render
from core.models import Post, Tag

# Create your views here.

def blogIndex(request):
    template = "blog.html"
    posts = Post.objects.all()
    tags = Tag.objects.all()

    data = {
        'posts': posts,
        'tags': tags
    }

    return render(request, template, data)

