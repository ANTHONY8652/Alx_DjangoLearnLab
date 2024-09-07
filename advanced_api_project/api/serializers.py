from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']
        
    def validate_publication_year(self, value):
        if value > datetime.datetime.now().year:
            return serializers.ValidationError("Year cannot be in the future")
        return value
    
# The AuthorSerializer includes nested serialization of the related Book model.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

# This allows displaying all books associated with an author in the API response.  
    class Meta:
        model = Author
        fields = ['name', 'books']


        