from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializer import BookSerializer
from rest_framework.permissions import AllowAny ,IsAuthenticated


class Books_list (generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

class Books_list_create (generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    

class Book_detail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]