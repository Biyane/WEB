from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
# Create your models here.


# class User(AbstractUser):
#     username = models.CharField(max_length=20, unique=True)  #login field in Angular
#     password = models.CharField(max_length=30)
#     first_name = models.CharField(max_length=30)  # name field in Angular
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField(
#         unique=True,
#         max_length=254,
#     )
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email', 'password', 'first_name', 'last_name']
#
#     def __str__(self):
#         return '{}'.format(self.username)


class Categories(models.Model):
    name = models.CharField(max_length=50)


class Recipe(models.Model):
    name = models.CharField(max_length=50, blank=True)
    categoryId = models.ForeignKey(Categories, on_delete=models.CASCADE)
    ingredients = models.TextField(blank=True)
    description = models.TextField(blank=True)
    rating = models.IntegerField(blank=True, null=True)
    image = models.TextField(blank=True)

