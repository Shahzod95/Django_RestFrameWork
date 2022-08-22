from django.shortcuts import render
from rest_framework import viewsets

from api.serializers import BookSerializer, LibUserSerializer, RentBookSerializer
from .models import Book, LibUser, RentBook

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    

class LibUserViewSet(viewsets.ModelViewSet):
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializer

class RentBookViewSet(viewsets.ModelViewSet):
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer