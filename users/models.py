from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TimeStamp(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserProfile(TimeStamp):
    DEFAULT_PROFILE_PIC_URl = "https://mywebsite.com/placeholder.png"
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    
    profile_pic_url = models.CharField(max_length=256, default=DEFAULT_PROFILE_PIC_URl)
    bio = models.CharField(max_length=256, blank=True)
    is_verified = models.BooleanField(default=True)