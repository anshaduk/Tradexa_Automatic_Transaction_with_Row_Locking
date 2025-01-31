from django.db.models.signals import pre_delete
from django.dispatch import receiver
from . models import Order

@receiver(pre_delete,sender=Order)
def release_stock_on_order_cancel(sender,instance,**kwargs):
    if not instance.confirmed:
        for product in instance.products.all():
            product.stock += instance.quantity
            product.save()
