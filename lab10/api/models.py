from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.models import User
# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    city = models.CharField(max_length=200)
    address = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.SET_NULL,null=True)

    # def array_json(self):
    #     for i in range(10):
    #         {
    #             'name': self.name + str(i),
    #             'description': self.description + str(i),
    #             'salary': 2 * i,
    #             'company': Company.objects.get(pk=1),
    #         }

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
        }
