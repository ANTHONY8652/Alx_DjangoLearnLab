from django.shortcuts import render
from rest_framework import generics, filters, status
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from django.urls import reverse
from rest_framework.test import APITestCase

#List all boooks
#Book list view with filtering
class BookListView(generics.ListApiView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

#Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

"""Create a new mbook"""
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

#Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

"""Delete a book"""
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookAPITests(APITestCase):
    def setUp(self):
        self.book1 = Book.objects.create(title="Book One", author="Author Anthony", publication_year=2023)
        self.book2 = Book.objects.create(title="Book Two", author="Author Githinji", publication_year=2024)
        self.list_url = reverse('book_list')
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})
    
    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": "Author C",
            "publication_year": 2022
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, "New Book")
    
    def test_get_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Verify the number of books returned
    
    def test_update_book(self):
        data = {
            "title": "Updated Book",
            "author": "Author A",
            "publication_year": 2020
        }
        response = self.client.put(self.detail_url(self.book1.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")
        
    def test_delete_book(self):
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        response = self.client.get(f'{self.list_url}?author=Author A')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], "Author A")
    
    def test_search_books_by_title(self):
        response = self.client.get(f'{self.list_url}?search=Book One')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book One")
    
    def test_order_books_by_publication_year(self):
        response = self.client.get(f'{self.list_url}?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2020)
    
    def test_access_control(self):
        # Assuming permissions are set, test unauthorized access
        response = self.client.get(self.list_url)  # No auth headers set
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)








    
# Create your views here.
