from django.db import models
from .models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

if __name__ == "__main__":

    #Query all books by a specific author
    author_books = query_books_by_author("J.K Rowling")
    print("Books by J.K Rowling:", [book.title for book in author_books])

    #List all books in a library
    library_books = list_books_in_library("Central Library")
    print("Books in Central Library:", [book.title for book in library_books])

    #retrieve the librarian for a library
    librarian = get_librarian_for_library("Central Library")
    print("Librarian of Central Library:" librarian.name if librarian else "No librarian assigned")