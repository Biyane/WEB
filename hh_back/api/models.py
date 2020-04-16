from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    city = models.CharField(max_length=20)
    address = models.TextField

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    city = models.FloatField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
