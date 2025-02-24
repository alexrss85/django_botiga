from django.db import models

# Create your models here.
class Order(models.Model):
    status_choice = [("pendent","Pendent"), ("completat","Completat"), ("Cancel·lat","Cancel·lat")]

    user_id = models.ForeignKey('cart.User', on_delete=models.CASCADE)
    total_price = models.IntegerField()
    status = models.CharField(max_length=20, choices=status_choice, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)