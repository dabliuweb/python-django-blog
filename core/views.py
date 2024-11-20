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

def post(request, id):
    template = "post.html"
    post = Post.objects.get(id=id)
    relateds = Post.objects.filter(tags__in=post.tags.all()).exclude(id=id).distinct()

    try:
        next_post = post.get_next_by_created_at()
    except Post.DoesNotExist:
        next_post = None

    try:
        previous_post = post.get_previous_by_created_at()
    except Post.DoesNotExist:
        previous_post = None

    data = {
        'post': post,
        'relateds': relateds,
        'next_post': next_post,
        'previous_post': previous_post
    }

    return render(request, template, data)
