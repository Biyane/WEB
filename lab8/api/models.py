from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count
        }