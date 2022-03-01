import base64
from io import BytesIO

from PIL import Image
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response

from shops.models import Category
from shops.models import Product
from shops.models import Shop
from shops.serializers import ShopSerializer, CategorySerializer, ProductSerializer


class ShopViewSet(viewsets.ViewSet):
    permission_classes_by_action = {'create': [AllowAny],
                                    'list': [AllowAny],
                                    'retrieve': [AllowAny],
                                    'update': [IsAuthenticated],
                                    'destroy': [IsAdminUser]}

    def list(self, request):
        queryset = Shop.objects.all()
        serializer = ShopSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        try:
            shop = Shop.objects.get(slug=slug)
            serializer = ShopSerializer(shop)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Shop.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, slug=None):
        try:
            shop = Shop.objects.get(slug=slug)
            serializer = ShopSerializer(shop, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Shop.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, slug=None):
        try:
            shop = Shop.objects.get(slug=slug)
            shop.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Shop.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve_by_user(self, request, user_id=None):
        try:
            shop = Shop.objects.get(user=user_id)
            serializer = ShopSerializer(shop)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Shop.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve_products(self, request, slug=None):
        try:
            shop = Shop.objects.get(slug=slug)
            products = Product.objects.filter(shop=shop)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Shop.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class ProductViewSet(viewsets.ViewSet):
    permission_classes_by_action = {'create': [IsAuthenticated],
                                    'list': [AllowAny],
                                    'retrieve': [AllowAny],
                                    'retrieve_qr_code_png': [AllowAny],
                                    'retrieve_qr_code_pdf': [AllowAny],
                                    'update': [IsAuthenticated],
                                    'destroy': [IsAuthenticated]}

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        try:
            product = Product.objects.get(slug=slug)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, slug=None):
        try:
            product = Product.objects.get(slug=slug)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, slug=None):
        try:
            product = Product.objects.get(slug=slug)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve_qr_code_png(self, request, slug=None):
        try:
            product = Product.objects.get(slug=slug)
            return Response("data:image/png;base64, " + product.base_64_qr_code)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve_qr_code_pdf(self, request, slug=None):
        try:
            product = Product.objects.get(slug=slug)
            pdf = BytesIO()
            img = Image.open(BytesIO(base64.b64decode(product.base_64_qr_code)))
            img.save(pdf, format='PDF')
            pdf.seek(0)
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="' + product.slug + '.pdf"'
            return response
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [IsAdminUser],
                                    'list': [AllowAny],
                                    'retrieve': [AllowAny],
                                    'update': [IsAdminUser],
                                    'destroy': [IsAdminUser]}

    def get_serializer_class(self):
        return CategorySerializer

    def list(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        try:
            category = Category.objects.get(slug=slug)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, slug=None):
        try:
            category = Category.objects.get(slug=slug)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, slug=None):
        try:
            category = Category.objects.get(slug=slug)
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
