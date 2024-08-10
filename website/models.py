from django.db import models

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
