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

class REcipeManager(models.Manager):
    def get_high_rating_queryset(self):
        return super().get_queryset().filter(rating__gte=3)

    def get_null_queryset(self):
        return super().get_queryset().filter(description=None)


class Categories(models.Model):
    name = models.CharField(max_length=50)


class Recipe(models.Model):
    name = models.CharField(max_length=50, blank=True, default="No Name")
    categoryId = models.ForeignKey(Categories, on_delete=models.CASCADE)
    ingredients = models.TextField(blank=True, default="No ingredients")
    description = models.TextField(blank=True)
    rating = models.IntegerField(blank=True, null=True)
    image = models.TextField(blank=True)
    recipe_objects = REcipeManager()
    objects = models.Manager()
