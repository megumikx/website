from django.db import models
from cloudinary.models import CloudinaryField


class Product(models.Model):
    BRAND_CHOICES = [
        ('obertos', 'Obertos'),
        ('well', 'Well'),
        ('djin', 'Джинн'),
        ('puxliykrolik', 'Пухлый кролик'),
        ('boombubble', 'Bubbe Boom'),
        ('chokki', 'ChoK-ki'),
    ]

    name = models.CharField(max_length=150)
    brand = models.CharField(
        max_length=20,
        choices=BRAND_CHOICES
    )
    description = models.TextField(blank=True)
    image = CloudinaryField('image', blank=True, null=True)
    image_url = models.URLField(
        'Ссылка на изображение Cloudinary',
        blank=True
    )
    weight = models.CharField(max_length=50, blank=True)
    flavor = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
