from django.db import models
from profiles.models import Profile
# Create your models here.
class report(models.Model):
    name=models.CharField(max_length=120)
    image=models.ImageField(upload_to='Report',blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    remake=models.TextField()
    author= models.ForeignKey(Profile,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.name)