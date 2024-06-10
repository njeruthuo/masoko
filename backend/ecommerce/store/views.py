# store/views.py
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Product, Order
from .serializers import UserSerializer, ProductSerializer, OrderSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
