from django.db import models
from django.urls import reverse
from django_google_maps import fields as map_fields
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.

get_positions = {
    "محرر":"محرر",
    "كاتب":"كاتب",
    "محررة":"محررة",
    "كاتبة":"كاتبة"
}

class Category(models.Model):

    name = models.CharField(max_length=60, verbose_name="التصنيف")
    eng_name = models.CharField(max_length=60, null=True, verbose_name="الاسم باللغة الانجليزية")
    img = models.ImageField(upload_to='categories', height_field=None, width_field=None, max_length=None, verbose_name="الصورة")
    order = models.IntegerField(verbose_name="الصورة")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", args=(self.eng_name,))


class Author(models.Model):

    name = models.CharField(max_length=50, verbose_name="الاسم")
    img = models.ImageField(upload_to="avatars", height_field=None, width_field=None, max_length=None, blank=True, verbose_name="الصورة")
    desc = models.TextField(verbose_name="الوصف")
    pos = models.CharField(max_length=30, choices=get_positions, verbose_name="المنصب") 

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=2000, verbose_name="العنوان الداخلي" )
    ext_name = models.CharField(max_length=100, verbose_name="العنوان الخارجي")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="posts", verbose_name="التصنيف")
    author = models.ManyToManyField("author", verbose_name=_("الكاتب"))
    date = models.DateField(auto_now=False, auto_now_add=True)
    slug = models.SlugField()
    main_img = models.ImageField(upload_to="posts", height_field=None, width_field=None, max_length=None, verbose_name="الصورة الخارجية")
    content = models.TextField(verbose_name="المحتوي")
    desc = models.TextField(verbose_name="المختصر ")
    address = map_fields.AddressField(max_length=200, null=True, blank=True, verbose_name="العنوان")
    geolocation = map_fields.GeoLocationField(max_length=100, null=True, blank=True, verbose_name="الموقع الجغرافي")
    tags = models.ManyToManyField("Tag", verbose_name="العلامة")
    
    Egyptian = models.IntegerField(null=True, blank=True, verbose_name="مصري")
    Egyptian_student = models.IntegerField(null=True, blank=True, verbose_name="طالب مصري")
    Foreign = models.IntegerField(null=True, blank=True, verbose_name="أجنبي")
    Foreign_student = models.IntegerField(null=True, blank=True, verbose_name="طالب أجنبي")

    open_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name="يفتح")
    closing_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True, verbose_name="يغلق")


    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", args=(self.slug,))


class Comment(models.Model):

    post = models.ForeignKey("Post", verbose_name="post", on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    body = models.CharField(max_length=300) 

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['date']

    def __str__(self):
        return self.user.first_name

class Tag(models.Model):

    caption = models.CharField(max_length=50, verbose_name="العلامة")
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse("Tag_detail", kwargs={"pk": self.pk})