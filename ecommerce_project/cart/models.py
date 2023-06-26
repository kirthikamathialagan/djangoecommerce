from django.db import models

from shopapp.models import Product


# Create your models here.
class Cart (models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    created_id=models.DateField(auto_now_add=True)
    class meta:
        db_table='cart'
        ordering=('created_id',)
    def __str__(self):
        return f"{self.cart_id}"

class Cart_Item(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    class meta:
        db_table='cart_item'
    def sub_total (self):
        return self.product.price * self.quantity
    def __str__(self):
        return f"{self.product}"


