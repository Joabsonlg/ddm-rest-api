from django.db import models
from autoslug import AutoSlugField
from users.models import User

# Create a model for shops
class Shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = AutoSlugField(unique=True, always_update=False, populate_from='name')
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True)
    website = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'

    def get_absolute_url(self):
        return f'/{self.slug}/'

# create a model for categories
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(unique=True, always_update=False, populate_from='name')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return f'/{self.slug}/'

# Create a model for products
class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = AutoSlugField(unique=True, always_update=False, populate_from='name')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=200)
    qr_code = models.ImageField(upload_to='images/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def get_image_url(self):
        return self.qr_code.url