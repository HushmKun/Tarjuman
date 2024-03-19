from django.contrib import admin
from .models import Author, Category, Post

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "img", "desc"]

@admin.register(Category)
class Admin(admin.ModelAdmin):
    list_display = ["name", "eng_name"]
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", 'desc', "author", "date", "slug", "content", "main_img"]

