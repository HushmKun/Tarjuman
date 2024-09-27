from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import *
from .serializers import AuthorsSerializer, PostsSerializer, PostDetailsSerializer
# Create your views here.

class AuthorView(APIView):
   def get (self, request):
       authors = Author.objects.all()
       serializer = AuthorsSerializer(authors, many=True)
       return Response({"author":serializer.data})

class PostsView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response({"posts":serializer.data})

class PostDetailView(APIView):   
   def get(self, request, slug):
       saved_article = get_object_or_404(Post.objects.all(), slug=slug)
       serializer = PostDetailsSerializer(instance=saved_article)
       return Response({"Article": serializer.data})