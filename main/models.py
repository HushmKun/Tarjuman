from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=60)
    eng_name = models.CharField(max_length=60, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


class Author(models.Model):

    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="avatars", height_field=None, width_field=None, max_length=None)
    desc = models.TextField()

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})


class Post(models.Model):

    title = models.CharField(max_length=150)
    category = models.ForeignKey("Category", on_delete=models.CASCADE,related_name="posts")
    author = models.ForeignKey("author", on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=True)
    slug = models.CharField(max_length=50)
    main_img = models.ImageField(upload_to="posts", height_field=None, width_field=None, max_length=None)
    content = models.TextField()
    desc = models.TextField()


    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})
