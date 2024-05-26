from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    bio = models.TextField(max_length=500, blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=30, blank=True)
    genre = models.CharField(max_length=100, choices=[
        ('rap', 'Rap'),
        ('rnb', 'R&B'),
        ('pop', 'Pop'),
        ('house', 'House'),
        ('edm', 'EDM'),
        ('rock', 'Rock'),
        ('jazz', 'Jazz'),
        ('indie', 'Indie'),
        ('other', 'Other'),
    ], default='Not Specified')

    def __str__(self):
        return self.user.username
