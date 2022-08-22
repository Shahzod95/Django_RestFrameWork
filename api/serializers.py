from dataclasses import field
import imp
from pyexpat import model
from rest_framework import serializers
from . import models
from .models import Book, LibUser, RentBook

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class LibUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class RentBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'