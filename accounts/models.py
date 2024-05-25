from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    bio = models.TextField(max_length=500, blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.email
