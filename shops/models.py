from django.db import models
from autoslug import AutoSlugField
from users.models import User
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
import base64

# Create a model for shops
class Shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = AutoSlugField(unique=True, always_update=False, populate_from='name')
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True)
    website = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

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
    base_64_qr_code = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def save(self, *args, **kwargs):
        fname = f'{self.name}.png'
        buffer = BytesIO()
        qr = qrcode.QRCode(
            version=12,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=8
        )
        qr.add_data(self.description)
        qr.make()
        qrcode_img = qr.make_image()
        qrcode_img.save(buffer, format='PNG')
        encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
        self.base_64_qr_code = encoded
        super().save(*args, **kwargs)