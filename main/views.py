from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author, Category, Comment
import random


# Create your views here.


def home(request):

    items = Post.objects.order_by("-date")[:20]

    context = {
        "main_post": items[0],
        "smaller_posts": items[1:3],
        "slider_posts": items[3:8],
        "editors_choice": items[8:14],
        "popular_stories": items[14:20],
    }
    return render(request, "main/index.html", context)


def category(request, cat):

    categories = Category.objects.all().order_by("order")
    category = categories.get(eng_name=cat)
    posts = category.posts.all().order_by("-date")
    paginator = Paginator(posts, 4)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_number)

    context = {
        "category": category,
        "categories": categories,
        "posts": posts,
        "page_obj": page_obj,
    }
    return render(request, "main/category.html", context)


def post(request, slug):
    categories = Category.objects.all().order_by("order")

    posts = Post.objects.all()
    post = posts.get(slug=slug)

    if request.method == "POST":

        print("Got into POST")
        
        if request.user.is_authenticated:
            comment = Comment(
                user=request.user, post=post, body=request.POST.get("body")
            )
            comment.save()
            
            
    try:
        next_posts, prev_posts = posts.order_by("?")[:2]
    except : 
        next_posts, prev_posts = None, None

    comments = Comment.objects.filter(post=post)

    context = {
        "categories": categories,
        "post": post,
        "prev_post": prev_posts,
        "next_post": next_posts,
        "comments": comments,
    }
    return render(request, "main/post_details.html", context)
