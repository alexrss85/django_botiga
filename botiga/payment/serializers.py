from rest_framework import serializers
from .models import Payment
from orders.models import Order  
from cart.models import User  

class PaymentSerializer(serializers.ModelSerializer):

    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # relaciona amb user per l'id
    order_id = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())  # relaciona amb order per id

    class Meta:
        model = Payment
        fields = ['num_tarjeta', 'data_caducitat', 'cvc', 'estat_pagament', 'user_id', 'order_id']