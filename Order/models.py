from django.db import models
from Product.models import product
from django.contrib.auth.models import User


class Cart(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    totalbill = models.IntegerField()
    status = models.CharField(max_length=30, default='Processing')
    order_date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
