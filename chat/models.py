from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

#conversation thread model
class ThreadModel(models.Model):
    #conversation thread model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")

    def __str__(self):
        return f"Thread between {self.user} and {self.receiver}"




class MessageModel(models.Model):
    #conversation thread model
    thread = models.ForeignKey(ThreadModel, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    body = models.CharField(max_length=2000)
    date = models.DateField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    

class Notification(models.Model):
    #message notification model
    to_user = models.ForeignKey(User, related_name='notification_to', on_delete=models.CASCADE, null=True)
    from_user = models.ForeignKey(User, related_name='notification_from', on_delete=models.CASCADE, null=True)
    thread = models.ForeignKey('ThreadModel', on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    date = models.DateField(default=timezone.now)
    user_has_seen = models.BooleanField(default=False)