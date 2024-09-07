from rest_framework import serializers
from .models import Author, Book, Publisher

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'country']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        publisher_data = validated_data.pop('publisher')
        
        author, created = Author.objects.get_or_create(**author_data)
        publisher, created = Publisher.objects.get_or_create(**publisher_data)
        
        book = Book.objects.create(author=author, publisher=publisher, **validated_data)
        return book