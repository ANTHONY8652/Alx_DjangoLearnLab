# CRUD Operations for the Book Model

## Introduction
This document details the CRUD (Create, Retrieve, Update, Delete) operations performed on the `Book` model within the `bookshelf` Django app. Each operation is accompanied by the relevant Python commands, explanations, and expected outcomes.

## 1. Create Operation
**Command**
```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()
"""Expected Output:
A new Book instance should be successfully created and stored in the database."""

## 2. Retrieve Operation
**Command**
```python
book = Book.objects.get(title="1984")
print(book)
"""Expected Output:
The details of the book with the title "1984" should be displayed."""

## 3. Update Operation
**Command**
```python
book.title = "Nineteen Eighty-Four"
book.save()
"""Expected Output:
The book’s title should be updated to "Nineteen Eighty-Four" in the database."""

## 4. Delete Operation
**Command**
```python
from bookshelf.models import Book
book.delete()
books = Book.objects.all()
print(books)
"""Expected Output:
The book should be deleted, and the retrieval query should return no results."""