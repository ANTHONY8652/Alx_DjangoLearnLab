# Create Operation

## Command:
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()

### Expected Output: A new Book instance should be successfully created and stored in the database.