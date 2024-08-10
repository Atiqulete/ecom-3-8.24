from django.db import models
from django.utils import timezone

# Create your models here.

class ContactInfo(models.Model):
    Name = models.CharField(max_length=300)
    Email = models.EmailField()
    Phone_Number = models.CharField(max_length=13)
    Subject = models.CharField(max_length=450)
    Message = models.TextField()

    class Meta:
       verbose_name_plural = "Contact-Infos" 
    def __str__(self):
        return self.Name

class Banner(models.Model):
    name_Promotions = models.CharField(max_length=300)
    intro_title1 = models.CharField(max_length=400,null=True, blank=True)
    intro_title2 = models.CharField(max_length=400,null=True, blank=True)
    old_price = models.CharField(max_length=14)
    new_price = models.CharField(max_length=14)
    new_price_sub = models.CharField(max_length=14)
    image = models.ImageField(upload_to='banner_image/')
    class Meta:
        verbose_name_plural =("Banner")

    def _str_(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, null=False)
    img = models.ImageField(upload_to='category_images/', null=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name 

class Brand(models.Model):
    name = models.CharField(max_length=50, null=False)
    img = models.ImageField(upload_to='category_images/', null=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Brands'

    def _str_(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='ProducImage')
    regular_price= models.PositiveIntegerField()
    discount_price= models.PositiveIntegerField(blank=True,null=True)
    descriptions =  models.TextField()
    aditional_descriptions =  models.TextField()
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural =("Products")

    def _str_(self):
        return self.name 