from enum import unique
from django.db import models

# Create your models here.



class Author(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True,default=None)
    password = models.CharField(max_length=255, default=None)

class Blog(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    picture = models.ImageField( default="test")
    author_id =models.ForeignKey(Author,on_delete=models.CASCADE)