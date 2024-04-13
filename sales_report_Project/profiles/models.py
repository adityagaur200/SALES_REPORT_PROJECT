from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)           #THIS CASCADE function IS USE TO AUTOMATICALLY DELETE USER PROFILE IF ITS DELETED
    Bio=models.TextField(default="no bio")
    image=models.ImageField(default="no_pic.png",upload_to="profile")
    created_date=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)

    def __str__(self):
        return f"Profile :{ self.user.username} "