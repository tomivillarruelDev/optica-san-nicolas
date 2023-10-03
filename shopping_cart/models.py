from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=4)
    size = models.CharField(max_length=64)
    image = models.ImageField(upload_to='products', blank=True)
    url = models.URLField(blank=True)


    def __str__(self):
        return f"{self.name} {self.price} {self.size}"