
from django.db import models
from cloudinary.models import CloudinaryField


class Product(models.Model):
    BRAND_CHOICES = [
        ('obertos', 'Obertos'),
        ('well', 'Well'),
        ('djin', 'Djin'),
    ]

    name = models.CharField(max_length=150)
    brand = models.CharField(
        max_length=20,
        choices=BRAND_CHOICES
    )
    description = models.TextField(blank=True)
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name
