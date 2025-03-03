from rest_framework import viewsets

from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer

from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def retrieve(self, request, pk=None):
        order = Order.objects.filter(pk=pk).first()

        if order:
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"Error": "No se ha encontrado la orden"}, status=status.HTTP_404_NOT_FOUND)


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer