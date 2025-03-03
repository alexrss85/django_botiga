from django.db import models

# Create your models here.
class Product(models.Model):
    nom = models.CharField(max_length=50)  
    descripcio = models.CharField(max_length=50) 
    preu = models.IntegerField()  
    stock = models.IntegerField()  
    categoria = models.CharField(max_length=30)
    marca = models.CharField(max_length=20)  

