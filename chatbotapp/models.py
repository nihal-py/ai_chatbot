from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    
    name = models.CharField(max_length=100, default='User')
    mobile_number = models.CharField(max_length=20, default='Nil')
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)


    @property
    def imageURL(self):
        try:
            url = self.profile_picture.url
        except:
            url = ''
        return  url
    

    def __str__(self):
        return self.username
    

class Chats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Chat with {self.user.username} on {self.date}"