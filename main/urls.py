from django.urls import path
from . import views

urlpatterns = [
    path("", views.coming_soon, name="coming"),
    path("home", views.home, name="home"),
    path("category/<str:cat>", views.category, name="category"),
    path("post/<slug:slug>", views.post, name="post"),
]

#! Need Recent & Popular & Editors Pick pages  
#! Author Page 
#! Categories Pages

