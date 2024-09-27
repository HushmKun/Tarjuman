from django.urls import path
from .views import AuthorView, PostsView, PostDetailView

app_name="api"

urlpatterns=[
   path('authors/', AuthorView.as_view()),
   path('posts/', PostsView.as_view()),
   path('post/<slug:slug>', PostDetailView.as_view()),
]