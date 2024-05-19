from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author, Category, Comment, Tag
import random
from django.conf import settings 


def get_footer():
        pharo = Post.objects.filter(category__eng_name="pharonic")
        coptic = Post.objects.filter(category__eng_name="coptic")
        islamic = Post.objects.filter(category__eng_name="islamic") 
        modern = Post.objects.filter(category__eng_name="modern")
        podcast = Post.objects.filter(category__eng_name="podcast")

        return [pharo, coptic, islamic, modern, podcast]


# Create your views here.


def home(request):

    items = Post.objects.exclude(tags__caption="مقالات").exclude(tags__caption="إفتتاحي").order_by("-date")[:3]
    articles = Post.objects.filter(tags__caption="مقالات")[:4]
    reports = Post.objects.filter(tags__caption="تقرير")[:5]
    news = Post.objects.filter(tags__caption="أخبار")
    static = get_footer()
    context = {
        "main_post": items[0] ,
        "smaller_posts": items[1:3] if 1 < len(items) else None,
        "slider_posts": news,
        "editors_choice": articles,
        "popular_stories": reports,
        "pharo":static[0],
        "coptic":static[1],
        "islamic":static[2],
        "modern":static[3],
        "podcast":static[4]
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

    static = get_footer()
    context = {
        "category": category,
        "categories": categories,
        "posts": posts,
        "page_obj": page_obj,
        "pharo":static[0],
        "coptic":static[1],
        "islamic":static[2],
        "modern":static[3],
        "podcast":static[4]
    }
    return render(request, "main/category.html", context)


def post(request, slug):
    categories = Category.objects.all().order_by("order")

    posts = Post.objects.all()
        
    post = get_object_or_404(Post, slug=slug)

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

    static = get_footer()
    context = {
        "category": Tag.objects.get(caption__exact='مقالات') in post.tags.all() ,
        "categories": categories,
        "post": post,
        "prev_post": prev_posts,
        "next_post": next_posts,
        "comments": comments,
        "google" : settings.GOOGLE_MAPS_API_KEY,
        "pharo":static[0],
        "coptic":static[1],
        "islamic":static[2],
        "modern":static[3],
        "podcast":static[4]
    }
    return render(request, "main/post_details.html", context)

def usage(request):
    static = get_footer()
    context = {
        "pharo":static[0],
        "coptic":static[1],
        "islamic":static[2],
        "modern":static[3],
        "podcast":static[4]
    }
    return render(request, "main/usage.html", context=context)
