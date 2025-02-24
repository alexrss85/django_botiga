from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=30)

class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.ForeignKey('catalog.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()