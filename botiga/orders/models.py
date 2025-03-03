
from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    ESTATS = [
        ('pendent', 'Pendent'),
        ('completat', 'Completat'),
        ('cancel·lat', 'Cancel·lat')]

    user_id = models.ForeignKey(User, on_delete=models.CASCADE) 
    total_price = models.DecimalField(max_digits=10, decimal_places=2) 
    status = models.CharField(max_length=20, choices=ESTATS, default='pendent')  
    created_at = models.DateTimeField(auto_now_add=True) 

  