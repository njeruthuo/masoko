# store/urls.py
from django.urls import path
from .views import UserList, ProductList, OrderList

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('orders/', OrderList.as_view(), name='order-list'),
]
