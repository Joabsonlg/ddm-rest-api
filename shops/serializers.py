from users.serializers import UserCreateSerializer
from rest_framework import serializers

from shops.models import Category, Product, Shop


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


class UserShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['user'] = UserCreateSerializer(read_only=True)
        return super(UserShopSerializer, self).to_representation(instance)
