from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.CharField(max_length=100)
    products = models.ManyToManyField(Product)
    quantity = models.PositiveIntegerField()
    confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    