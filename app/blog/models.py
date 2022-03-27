from enum import unique
from django.db import models

# Create your models here.



class Author(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

class Blog(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    picture = models.ImageField( default="test")
    author_id =models.ForeignKey(Author,on_delete=models.CASCADE)