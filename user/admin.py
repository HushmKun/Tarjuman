from django.contrib import admin
from .models import Profile

# Register your models here.


@admin.register(Profile)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["user", "profile_picture"]
