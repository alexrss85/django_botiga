from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=30)

class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(db_comment="Date time creation")