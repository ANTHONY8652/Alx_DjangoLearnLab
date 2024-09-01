# Authentication and Permissions Setup in Django REST Framework

## 1. Configure Authentication

### Steps:

1. **Add Token Authentication to Installed Apps:**
   - Edit `settings.py` to include `'rest_framework.authtoken'` in `INSTALLED_APPS`.
     ```python
     INSTALLED_APPS = [
         # Other apps
         'rest_framework',
         'rest_framework.authtoken',
     ]
     ```

2. **Run Migrations:**
   - Create database tables for token management.
     ```bash
     python manage.py migrate
     ```

3. **Update Authentication Settings:**
   - Add token authentication to `DEFAULT_AUTHENTICATION_CLASSES` in `settings.py`.
     ```python
     REST_FRAMEWORK = {
         'DEFAULT_AUTHENTICATION_CLASSES': [
             'rest_framework.authentication.TokenAuthentication',
         ],
     }
     ```

## 2. Generate and Use Tokens

### Steps:

1. **Create Token Retrieval Endpoint:**
   - Add URL pattern to `urls.py` for obtaining tokens.
     ```python
     from rest_framework.authtoken.views import obtain_auth_token
     from django.urls import path

     urlpatterns = [
         path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
     ]
     ```

2. **Obtain a Token:**
   - Send a POST request to `/api-token-auth/` with your username and password.
     **Request:**
     ```json
     {
         "username": "your_username",
         "password": "your_password"
     }
     ```
     **Response:**
     ```json
     {
         "token": "your_token"
     }
     ```

## 3. Define Permission Classes

### Steps:

1. **Use Permissions in Views:**
   - Apply permissions to your views to control access.
     ```python
     from rest_framework.permissions import IsAuthenticated

     class BookViewSet(viewsets.ModelViewSet):
         queryset = Book.objects.all()
         serializer_class = BookSerializer
         permission_classes = [IsAuthenticated]  # Only authenticated users can access
     ```

2. **Custom Permissions (Optional):**
   - Define and use custom permissions if needed.
     ```python
     from rest_framework.permissions import BasePermission

     class IsAuthor(BasePermission):
         def has_permission(self, request, view):
             return request.user and request.user.is_authenticated and request.user.is_author
     ```

## 4. Test Authentication and Permissions

### Steps:

1. **Test with Token:**
   - Use Postman or similar tools to send requests with the token in the `Authorization` header.
     ```
     Authorization: Token your_token
     ```

2. **Test Without Token:**
   - Verify that requests without a token are denied.

## 5. Documentation

### Summary:

- **Authentication Configuration:** Added token authentication to `INSTALLED_APPS`, migrated, and updated `DEFAULT_AUTHENTICATION_CLASSES`.
- **Token Generation:** Implemented endpoint for users to obtain tokens.
- **Permissions:** Configured permissions to restrict access based on authentication and roles.
- **Testing:** Validated API security with and without tokens.
