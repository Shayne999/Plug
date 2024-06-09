from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models import UUIDField
import uuid
from django.contrib.auth.models import User

# Create your models here.

User = get_user_model()

class Post(models.Model):
    #this is the post model
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images')
    video = models.FileField(upload_to='post_videos', null=True)
    caption = models.TextField()
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.user.username}'s Post"
    
class LikePost(models.Model):
    #this is the post like model
    post_id = UUIDField()
    username = models.CharField(max_length=400)

    def __str__(self):
        return self.username
    
class Favorite(models.Model):
    #this is the post favorite model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')