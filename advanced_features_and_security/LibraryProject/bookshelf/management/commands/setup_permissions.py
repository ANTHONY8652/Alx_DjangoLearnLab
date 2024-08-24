from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Permission
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Sets up initial permissions for users'

    def handle(self, *args, **kwargs):
        user, created = User.objects.get_or_create(username='testuser')
        if created:
            self.stdout.write(self.style.SUCCESS('User created'))

        try:
            can_add_book = Permission.objects.get(codename='can_add_book', content_type__app_label='bookshelf', content_type__model='book')
            can_delete_book = Permission.objects.get(codename='can_delete_book', content_type__app_label='bookshelf', content_type__model='book')
        except Permission.DoesNotExist:
            self.stdout.write(self.style.ERROR('Permissions not found'))
            return

        user.user_permissions.add(can_add_book, can_delete_book)
        self.stdout.write(self.style.SUCCESS('Permissions assigned'))
