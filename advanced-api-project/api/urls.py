from django.urls import path
from .views import BookCreateView, BookDeleteView, BookDetailView, BookListView, BookUpdateView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name = 'book-create-view'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update-view'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-destroy-view'),
]