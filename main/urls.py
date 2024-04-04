from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<str:cat>", views.category, name="category"),
    path("post/<slug:slug>", views.post, name="post")
]


