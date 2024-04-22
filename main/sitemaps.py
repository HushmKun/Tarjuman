from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1
    protocol = 'https'
 
    def items(self):
        return Post.objects.all()
    
    def lastmod(self, obj):
        return obj.date
    
    def location(self, obj):
        return '/post/%s' % (obj.slug)


class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'
 
    def items(self):
        return ['home']
 
    def location(self, item):
        return reverse(item)