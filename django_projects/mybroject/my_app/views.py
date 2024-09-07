from rest_framework import viewsets, filters
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().select_related('author', 'publisher')
    serializer_class = BookSerializer
    filter_backends = {filters.SearchFilter}
    search_fields = ['title', 'author__first_name', 'author__last_name', 'publisher__name']