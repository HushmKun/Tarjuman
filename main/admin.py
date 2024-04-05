from django.contrib import admin
from .models import Author, Category, Post, Comment, Tag
from django_summernote.admin import SummernoteModelAdmin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "img", "desc", "pos"]
    list_filter = ('pos',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "eng_name", "img", "order"]
    
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ["ext_name", "category", "desc", "author", "date", "main_img"]
    prepopulated_fields = {"slug": ("ext_name",)}
    summernote_fields = ('content','title')
    search_fields = ('ext_name', 'author')
    list_filter = ('category','author')
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'terrain'})},
    }
    fieldsets = [
        (
            "بيانات الخبر",
            {
                "fields": [ "category", "author", "tags", "main_img"],
            },
        ),
        (
          "محتوي الخبر",
            {
                "fields": ["title", "ext_name", "desc", "content", "address", ],
            },
        ),
        (
            "تكاليف الزيارة",
            {
                "fields": [("Egyptian", "Egyptian_student"), ("Foreign", "Foreign_student")],
            },
        ),
        (
            "مواعيد الزيارة",
            {
                "fields": ["open_time", "closing_time"],
            },
        ),
        (
            "لا تلمس",
            {
                "fields" : ["slug", "geolocation"]
            },
        ),
    ]

    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'body', 'post', 'date')
    list_filter = ('date','post')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('caption', )
