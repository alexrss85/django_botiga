from django.db import models

# Create your models here.
class Product(models.Model):
    nom = models.EmailField(unique=True, max_length=50)
    descripcio = models.CharField(max_length=20)
    preu = models.CharField(max_length=20)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=15)
    marca = models.CharField(max_length=15)