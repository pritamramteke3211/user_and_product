from django.db import models
from datetime import datetime

# Create your models here.

# Products app with Product model. Product : name, weight, price, created_at, updated_at Both of the apps should use two different databases. Create a form that an authenticated user can use to create a post.


class Product(models.Model):
    name = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to='product_img/' ,null=True,blank=True,default='product_img/cute.jfif')
    weight = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    
    
