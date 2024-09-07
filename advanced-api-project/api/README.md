## Filtering, Searching, and Ordering in Book API

### Filtering
You can filter the books based on title, author, or publication year using query parameters:
- `/api/books/?author=John`
- `/api/books/?publication_year=2020`

### Searching
Search functionality is enabled on the title and author fields:
- `/api/books/?search=Python`

### Ordering
You can order the book list by title or publication year:
- `/api/books/?ordering=title`
- `/api/books/?ordering=-publication_year` (for descending order)
## Testing Strategy for API Endpoints

### Overview
This document outlines the unit tests for the CRUD operations, filtering, searching, and ordering functionalities of the Book API.

### How to Run Tests
To run the tests, navigate to your project directory and execute:
```bash
python manage.py test api

