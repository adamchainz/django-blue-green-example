from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)


class Book(models.Model):
    title = models.CharField(max_length=1023)
    description = models.TextField()
    pages = models.IntegerField()
    isbn = models.IntegerField(null=True)
    authors = models.ManyToManyField("Author")
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
