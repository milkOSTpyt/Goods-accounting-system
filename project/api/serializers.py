from rest_framework.serializers import ModelSerializer
from app.models import Shop, Warehouse, Product, Category


class ProductSerializer(ModelSerializer):
    """Сериалайзер модели Product"""
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    """Сериалайзер модели Category"""
    class Meta:
        model = Category
        fields = '__all__'


class ShopSerializer(ModelSerializer):
    """Сериалайзер модели Shop"""
    class Meta:
        model = Shop
        fields = '__all__'


class WarehouseSerializer(ModelSerializer):
    """Сериалайзер модели Warehouse"""
    class Meta:
        model = Warehouse
        fields = '__all__'
