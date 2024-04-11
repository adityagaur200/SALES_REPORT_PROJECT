from django.db import models
from products.models import product
from customers.models import Customer
from profiles.models import Profile
from django.utils import timezone
from .utils import generate_code
# Create your models here.
class Position(models.Model):
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Price = models.FloatField(blank=True)
    Created = models.DateTimeField(blank=True)

    def save(self,*args,**kwargs):
        self.Price = self.product.price*self.Quantity
        return super().save(*args,**kwargs)

    def __str__(self):
        return f"id:{self.id},product: {self.product.name},quantity:{self.Quantity}"

class Sale(models.Model):
    Transaction_id=models.CharField(max_length=12,blank=True)
    Positions=models.ManyToManyField(Position)
    Total_Price=models.FloatField(blank=True,null=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Salesman = models.ForeignKey(Profile,on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"AMOUNT:{self.Total_Price}"
    
    def save(self,*args,**kwargs):
        if self.Transaction_id == "":
            self.Transaction_id = generate_code()
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args,**kwargs)
    def get_positions(self):
        return self.Positions.all()
    
class CSV(models.Model):
    file_name = models.FileField(upload_to="csvs")
    activated= models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.file_name)