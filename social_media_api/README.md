# Social Media API

## Overview

The **Social Media API** is a Django-based API designed for user management and authentication. It uses **Django REST Framework (DRF)** to provide functionalities such as user registration, login, and profile management. The API supports token-based authentication for secure interactions.

## Features

- **User Registration**: Create an account with a username, password, and optional email, bio, and profile picture.
- **User Login**: Log in and receive an authentication token.
- **Token-Based Authentication**: Use tokens to authenticate API requests.
- **Custom User Model**: Extends Django’s default user model to include:
  - `bio` - A text field for user biography.
  - `profile_picture` - An image field for profile photos.
  - `followers` - A many-to-many relationship for following users.
- **Profile Management**: Update profile details and manage followers.

## Setup

### 1. Clone the Repository

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/ANTHONY8652/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api
