from shops.models import Shop
from shops.models import Product
from shops.models import Category
from rest_framework import serializers

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('__all__')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')