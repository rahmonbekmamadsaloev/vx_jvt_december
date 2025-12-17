from django.urls import path
from .views import Book_detail, Books_list ,Books_list_create

urlpatterns = [
    path('books_list/', Books_list.as_view()),
    path('books/', Books_list_create.as_view()),
    path('books/<int:pk>/', Book_detail.as_view()),
]

