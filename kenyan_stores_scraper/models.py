from django.db import models
# from django.db.models.signals import pre_save
# from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
import time


class Products(models.Model):
    product_name = models.CharField(max_length=1000)
    product_image = models.CharField(max_length=10000)
    product_rating = models.IntegerField(default=0, blank=True, null=True)
    product_key_features = models.TextField()
    # slug = models.SlugField(unique=True)

    def __str__(self):
        return self.product_name.encode("utf-8")



class Jumia(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_price = models.IntegerField(default=0, null=False)
    product_warranty = models.CharField(max_length=200)
    product_discount = models.IntegerField(default=0,null=True,blank=True)
    product_seller = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=timezone.now,editable=False)
    return_time = models.CharField(max_length=1000)

    def __str__(self):
        return self.product_id.product_name.encode("utf-8") + "at " + str(self.product_price) + "as at " + str(self.timestamp)


class Avechi(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_price = models.IntegerField(default=0, null=False)
    product_warranty = models.CharField(max_length=200)
    product_discount = models.IntegerField(default=0,null=True,blank=True)
    product_seller = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=timezone.now,editable=False)
    return_time = models.CharField(max_length=1000)

    def __str__(self):
        return self.product_id.product_name.encode("utf-8") + "at " + str(self.product_price) + "as at " + str(self.timestamp)


class Killmall(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_price = models.IntegerField(default=0, null=False)
    product_warranty = models.CharField(max_length=200)
    product_discount = models.IntegerField(default=0, null=True,blank=True)
    product_seller = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=timezone.now,editable=False)
    return_time = models.CharField(max_length=1000)

    def __str__(self):
        return self.product_id.product_name.encode("utf-8") + "at " + str(self.product_price)+ "as at "+str(self.timestamp)


class TrackedProducts(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.product.id)

    class Meta:
        ordering = ['id']



