from .models import Sale
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


@receiver(m2m_changed,sender=Sale.Positions.through)
def calculate_total(sender,instance,action,**kwargs):
    print('action',action)

    Total_Price = 0
    if action == "post_add" or action == "post_remove":
        for item in instance.Positions():
            Total_Price += item.Price

    instance.Total_Price=Total_Price
    instance.save()