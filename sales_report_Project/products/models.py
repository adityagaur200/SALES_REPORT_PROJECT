from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=120)
    image=models.ImageField(upload_to='products',default="no_pic.png")
    price=models.FloatField(help_text="in INR")
    created_date=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.created_date.strftime('%d/%m/%Y')}"
    