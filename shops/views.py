from django.shortcuts import render
from shops.models import Shop
from shops.models import Product
from shops.models import Category
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import Http404

from shops.serializers import ShopSerializer
from shops.serializers import ProductSerializer
from shops.serializers import CategorySerializer

# Funcions for shops
@api_view(['GET'])
def getAllShops(request):
    shops = Shop.objects.all()
    serializer = ShopSerializer(shops, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getShop(request, slug):
    try:
        shop = Shop.objects.get(slug=slug)
    except Shop.DoesNotExist:
        raise Http404
    serializer = ShopSerializer(shop)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createShop(request):
    serializer = ShopSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateShop(request, slug):
    try:
        shop = Shop.objects.get(slug=slug)
    except Shop.DoesNotExist:
        raise Http404
    serializer = ShopSerializer(shop, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteShop(request, slug):
    try:
        shop = Shop.objects.get(slug=slug)
    except Shop.DoesNotExist:
        raise Http404
    shop.delete()
    return Response(status=204)

@api_view(['GET'])
def getProductsFromShop(request, slug):
    try:
        shop = Shop.objects.get(slug=slug)
    except Shop.DoesNotExist:
        raise Http404
    products = Product.objects.filter(shop=shop)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
# End of shops

# Funcions for products
@api_view(['GET'])
def getAllProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        raise Http404
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProduct(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        raise Http404
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteProduct(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        raise Http404
    product.delete()
    return Response(status=204)

@api_view(['GET'])
def getQRCode(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        raise Http404
    return Response(product.base_64_qr_code)

# End of products

# Funcions for categories
@api_view(['GET'])
def getAllCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCategory(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        raise Http404
    serializer = CategorySerializer(category)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createCategory(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateCategory(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        raise Http404
    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteCategory(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        raise Http404
    category.delete()
    return Response(status=204)
# End of categories