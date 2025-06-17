from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

# —————————— Product & related ——————————
class Product(models.Model):
    sku = models.SlugField(max_length=50, unique=True, blank=True, help_text="Stock Keeping Unit")
    title       = models.CharField(max_length=255)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image       = models.ImageField(upload_to='products/')

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = slugify(self.title).upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Parameter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='parameters')
    key     = models.CharField(max_length=100)
    value   = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Product Parameter'
        verbose_name_plural = 'Product Parameters'

    def __str__(self):
        return f"{self.key}: {self.value}"

# —————————— Industry Solution & related ——————————
class Solution(models.Model):
    title       = models.CharField(max_length=255)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image       = models.ImageField(upload_to='solutions/')

    def __str__(self):
        return self.title

class SuggestedProduct(models.Model):
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE, related_name='suggested_products')
    name     = models.CharField(max_length=100)
    note     = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Suggested Product'
        verbose_name_plural = 'Suggested Products'

    def __str__(self):
        return self.name

# —————————— News ——————————
class News(models.Model):
    title       = models.CharField(max_length=255)
    slug        = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(help_text="List‐page summary")
    content     = models.TextField(blank=True)
    image       = models.ImageField(upload_to='news/', blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            # auto-generate slug from title
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
