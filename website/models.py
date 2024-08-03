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