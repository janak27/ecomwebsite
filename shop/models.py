# from ecom.shop.views import checkout
from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class products(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        verbose_name = "Product"

class order(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    total = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Order"