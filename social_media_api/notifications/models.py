from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone

class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notifications', on_delete=models.CASCADE)
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='actor', on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_object_id = models.PositiveIntegerField()
    target= GenericForeignKey('target_content_type', 'target_object_id')
    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.actor.username} {self.verb} {self.target}'

# Create your models here.
