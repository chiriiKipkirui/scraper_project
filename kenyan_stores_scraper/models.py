from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone
import time


class Products(models.Model):
    product_name = models.CharField(max_length=1000)
    product_image = models.CharField(max_length=10000)
    product_rating = models.IntegerField(default=0, blank=True, null=True)
    product_key_features = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.product_name


def create_new_slug(instance,new_slug=None):
    slug = slugify(instance.product_name[:10])
    if new_slug is not None:
        slug = new_slug
    qs = Products.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug= "%s-%s" %(slug,qs.first().id)
        return create_new_slug(instance,new_slug=new_slug)
    return slug


def product_pre_save_ceiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_new_slug(instance)


pre_save.connect(product_pre_save_ceiver,sender=Products)


class Jumia(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_price = models.IntegerField(default=0, null=False)
    product_warranty = models.CharField(max_length=200)
    product_discount = models.IntegerField(default=0,null=True,blank=True)
    product_seller = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=timezone.now,editable=False)
    return_time = models.IntegerField()

    def __str__(self):
        return self.product_id.product_name + "at " + str(self.product_price) + "as at " + str(self.timestamp)


class Avechi(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_price = models.IntegerField(default=0, null=False)
    product_warranty = models.CharField(max_length=200)
    product_discount = models.IntegerField(default=0,null=True,blank=True)
    product_seller = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=timezone.now,editable=False)
    return_time = models.IntegerField()

    def __str__(self):
        return self.product_id.product_name + "at " + str(self.product_price) + "as at " + str(self.timestamp)


class Killmall(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_price = models.IntegerField(default=0, null=False)
    product_warranty = models.CharField(max_length=200)
    product_discount = models.IntegerField(default=0, null=True,blank=True)
    product_seller = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(default=timezone.now,editable=False)
    return_time = models.IntegerField()

    def __str__(self):
        return self.product_id.product_name + "at " + str(self.product_price)+ "as at "+str(self.timestamp)





