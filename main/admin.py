from django.contrib import admin
from .models import Author, Category, Post

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "img", "desc"]

@admin.register(Category)
class Admin(admin.ModelAdmin):
    list_display = ["name"]
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "date", "slug", "content", "main_img"]

