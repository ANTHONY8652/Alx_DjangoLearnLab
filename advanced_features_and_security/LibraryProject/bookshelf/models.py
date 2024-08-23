from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_delete_book", "Can delete book"),
            ("can_change_book", "Can change book")
        ]
    

class CustomUserManager(BaseUserManager):
    def create_user(self,username, email, date_of_birth=None, password=None, **extra_fields):
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, date_of_birth=None, password=None, **extra_fields):
        user = self.create_user(
            username=username,
            email=email,
            date_of_birth=date_of_birth,
            password=password,
            **extra_fields
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True)
    objects = CustomUserManager()
    
    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_view", "Can view posts"),
            ("can_create", "Can create posts"),
            ("can_edit", "Can edit posts"),
            ("can_delete", "Can delete posts")
        ] 

    def __str__(self):
        return self.title     
    
# Create your models here.
