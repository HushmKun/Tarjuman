from django.db import models
from django.contrib.auth.models import User
from PIL import Image  # We'll use Pillow for image handling

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to="profile_pics", default="avatars/avatar.png"
    )

    def __str__(self):
        return f"{self.user.username} Profile"
