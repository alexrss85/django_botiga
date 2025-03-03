from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Payment, User, Order
from .serializers import PaymentSerializer
from datetime import datetime, date
from rest_framework.exceptions import ValidationError


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        # agafar id de l'usuari
        user_id = self.request.data.get('user_id')

        # veure si existeix a la bbdd
        if not User.objects.filter(id=user_id).exists():
            return Response(
                {"error": "L'usuari no existeix"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # obtenim l'usuari
        user = User.objects.get(id=user_id)

        # verifiquem la tarjeta
        num_tarjeta = self.request.data.get('num_tarjeta')
        data_caducitat = self.request.data.get('data_caducitat')
        cvc = self.request.data.get('cvc')

        verificar, mensaje = verificar_tarjeta(num_tarjeta, data_caducitat, cvc)
        if not verificar:
            raise ValidationError(mensaje)

        # obtenim l'id del order desde el payement
        order_id = self.request.data.get('order_id')

        # verifiquem que existeix
        if not Order.objects.filter(id=order_id).exists():
            return Response(
                {"error": "L'ordre no existeix"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # agafem l'ordre
        order = Order.objects.get(id=order_id)

        # guardem el payment amb les dades correctes
        payment = serializer.save(user_id=user, order_id=order)

        # si es completa el pagament actualizem l'estat de l'ordre
        if payment.estat_pagament == 'completat':
            order.status = 'completat'
            order.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


def verificar_tarjeta(num_tarjeta, data_caducitat, cvc):
    # num_trajeta de 16 dígits
    if not num_tarjeta.isdigit() or len(num_tarjeta) != 16:
        return False, "Número de targeta invàlid"

    # cvc de 3 dígits
    if not cvc.isdigit() or len(cvc) != 3:
        return False, "CVC invàlid"

    # mirem que estigui caducada
    try:
        data_caducitat = datetime.strptime(data_caducitat, '%Y-%m-%d').date()
    except ValueError:
        return False, "La data de caducitat no té el format correcte"

    if data_caducitat < date.today():
        return False, "La targeta ha caducat"

    return True, "Dades vàlides"
