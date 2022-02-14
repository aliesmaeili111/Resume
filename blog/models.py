from statistics import mode
from django.db import models
# Create your models here.


class Article(models.Model):
    age = models.IntegerField()
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.TextField()
    status = models.BooleanField()
    id_tel = models.CharField(max_length=25)
    
    def __str__(self) :
        return self.email
    
    
class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    def __str__(self) :
        return self.name
    
    