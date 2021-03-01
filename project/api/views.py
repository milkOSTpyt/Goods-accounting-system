from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from app.models import Product, Category, Shop, Warehouse
from .serializers import (ProductSerializer,
                          CategorySerializer,
                          ShopSerializer,
                          WarehouseSerializer)


class ProductViewSet(ModelViewSet):
    """CRUD товара"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(ModelViewSet):
    """CRUD котегории"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ShopViewSet(ModelViewSet):
    """CRUD магазина"""
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticated]


class WarehouseViewSet(ModelViewSet):
    """CRUD склада"""
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [permissions.IsAuthenticated]


class SoldOutProduct(ListAPIView):
    """Вывод списка проданных товаров + фильтры"""
    queryset = Product.objects.filter(sold_out=True)
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'shop', 'category', 'warehouse']
