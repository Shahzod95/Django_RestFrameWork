from pyexpat import model
from unicodedata import name
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)

class LibUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class RentBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(LibUser, on_delete=models.CASCADE)
    rentDate = models.DateTimeField(auto_now_add=True)
    reterneddate = models.DateTimeField(null=True, blank=True)