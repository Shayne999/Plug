from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models import UUIDField
import uuid

# Create your models here.

User = get_user_model()

class Post(models.Model):
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
    post_id = UUIDField()
    username = models.CharField(max_length=400)

    def __str__(self):
        return self.username