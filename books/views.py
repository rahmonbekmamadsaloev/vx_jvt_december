from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics
from .models import Book
from .serializer import BookSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

CACHE_TTL = 60  # время кэширования в секундах

class Books_list(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


    @method_decorator(cache_page(CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        print("🚀 dispatch вызван")
        return super().dispatch(*args, **kwargs)


class Books_list_create(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [IsAuthenticated]


class Book_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [IsAuthenticated]
    

