from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post, Category

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

class CategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.4
    protocol = 'https'
 
    def items(self):
        return Category.objects.all()
    
    def lastmod(self, obj):
        return Category.order
    
    def location(self, obj):
        return '/category/%s' % (obj.eng_name)

class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'
 
    def items(self):
        return ['home']
 
    def location(self, item):
        return reverse(item)