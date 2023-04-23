from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to='product_image/')
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_length=7, max_digits=2)
    description = models.TextField()

    def __str__(self):
        return self.name
