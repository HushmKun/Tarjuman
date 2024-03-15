from django.shortcuts import render
from .models import Post, Author, Category

# Create your views here.

def coming_soon(request):
    return render(request, "coming_soon.html")

def home(request):
    pos = Post.objects.all()[0]
    context = {
        "main_post" : pos, 
        "smaller_posts" : [pos, pos],
        "slider_posts" : [pos, pos, pos, pos, pos],
        "editors_choice" : [pos, pos, pos, pos, pos, pos],
        "popular_stories": [pos, pos, pos, pos, pos, pos,]
    }
    return render(request, 'main/index.html', context)
