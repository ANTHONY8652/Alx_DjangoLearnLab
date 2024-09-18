from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model

class PostTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser1', password='testpass10')
        self.client.login(username='testuser1', password='testpass10')

    def test_create_post(self):
        response = self.client.post('api/posts/', {'title': 'Test Post', 'content': 'Test Content'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)

# Create your tests here.
