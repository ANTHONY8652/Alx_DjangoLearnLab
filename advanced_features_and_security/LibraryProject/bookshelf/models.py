from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return self.title
    
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True)
    
    def __str__(self):
        return self.username

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
        
    
# Create your models here.
