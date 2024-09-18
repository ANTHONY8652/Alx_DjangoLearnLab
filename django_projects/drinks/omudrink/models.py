from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
