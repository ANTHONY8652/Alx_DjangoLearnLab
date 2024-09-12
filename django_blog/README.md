## User Authentication System

### Features
- **Registration:** Users can sign up with a username and email.
- **Login:** Authenticated users can log in.
- **Logout:** Users can log out of their session.
- **Profile Management:** Authenticated users can view and update their profile.

### Testing Instructions
1. Register a new user using the `/register` page.
2. Log in with the new user credentials at `/login`.
3. Access the profile page `/profile` to view and update user details.
4. Logout from the session using `/logout`.

### Security
- All sensitive actions are protected with CSRF tokens.
- Passwords are securely hashed using Django’s default hashing mechanism.
