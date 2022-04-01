from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
        

class User(AbstractUser):
    """user name model"""
    username = None
    email = models.EmailField(_('email address'),unique=True)
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=[]
    objects = UserManager()


class Shoes(models.Model):
    name = models.CharField(max_length=255)
    size = models.FloatField()
    color = models.CharField(max_length=255)
    price = models.FloatField()
    price_bought = models.FloatField()
    price_selled = models.FloatField() 
    date_received = models.DateTimeField()
    date_selled = models.DateTimeField()
    quantity = models.IntegerField()
    damaged = models.BooleanField()
    selled = models.BooleanField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

