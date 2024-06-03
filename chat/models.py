from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

#conversation thread model
class ThreadModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")

    def __str__(self):
        return f"Thread between {self.user} and {self.receiver}"




#message model
class MessageModel(models.Model):
    thread = models.ForeignKey(ThreadModel, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    body = models.CharField(max_length=2000)
    date = models.DateField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    