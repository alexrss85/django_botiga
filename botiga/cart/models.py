from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=30)
    constrasenya = models.CharField(max_length=20, default=1234)
    