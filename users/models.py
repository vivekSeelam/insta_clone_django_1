from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=256, null=False)
    email = models.EmailField(max_length=256, null=False, unique=True)
    phone_num = models.CharField(max_length=256, null=False, unique=True)
    password = models.CharField(max_length=55, null=False)
    is_active = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class UserProfile(models.Model):
    DEFAULT_PROFILE_PIC_URl = "https://mywebsite.com/placeholder.png"

    profile_pic_url = models.CharField(max_length=256, default=DEFAULT_PROFILE_PIC_URl)
    bio = models.CharField(max_length=256, blank=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
