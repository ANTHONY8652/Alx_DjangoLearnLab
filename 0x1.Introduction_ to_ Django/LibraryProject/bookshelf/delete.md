# Delete Operation
## Command:
from bookshelf.models import Book
book.delete()
books = Book.objects.all()
print(books)
### Expected Output: The book should be deleted, and the retrieval query should return no results.