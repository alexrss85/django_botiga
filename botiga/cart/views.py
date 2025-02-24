"""
from rest_framework.response import Response
from rest_framework.decorators import api_view
"""
from rest_framework import viewsets

from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer

from rest_framework.response import Response
from rest_framework import status

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    """
    def list(self, request):
        cart_items = CartItem.objects.all()
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        cart_item = CartItem.objects.filter(pk=pk).first()

        if cart_item:
            serializer = CartItemSerializer(cart_item, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"Error": "No se ha encontrado el item del carrito"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        cart_item = CartItem.objects.filter(pk=pk).first()

        if not cart_item:
            return Response({"Error": "No se ha encontrado el item del carrito"}, status=status.HTTP_404_NOT_FOUND)
        
        cart_item.delete()
        return Response({"Mensaje": "Item borrado del carrito con éxito"}, status=status.HTTP_204_NO_CONTENT)
    """

"""
@api_view(['GET'])
def getCarts(request):
    carts = Cart.objects.all()
    serializer = CartSerializer(carts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createCart(request):
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
"""