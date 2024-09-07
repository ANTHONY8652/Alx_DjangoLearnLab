from django.db import models

# The Author model represents a writer of books, identified by a unique name.
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
# It has a one-to-many relationship with the Book model via a ForeignKey.   
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

# Create your models here.
