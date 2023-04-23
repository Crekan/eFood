from django.db import models


class Category(models.Model):
    image = models.ImageField(upload_to='category_image/', blank=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='product_image/')
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
