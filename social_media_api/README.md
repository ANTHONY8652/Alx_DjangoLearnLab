# Social Media API

## Overview

The **Social Media API** is a Django-based API that provides essential functionality for managing users. It includes user registration, login, and profile management with token-based authentication. This API uses **Django REST Framework (DRF)** for building and handling API requests.

## Features

- **User Registration**: Allows users to create an account with a username, password, and optional email, bio, and profile picture.
- **User Login**: Users can log in to obtain an authentication token.
- **Token-Based Authentication**: Secures API interactions using tokens issued upon login or registration.
- **Custom User Model**: Extends Django’s default user model to include additional fields and functionalities.
- **Profile Management**: Users can update their profile details and manage followers.

## Setup

### 1. Clone the Repository

First, clone the project repository and navigate into the project directory:

```bash
git clone https://github.com/YOUR_USERNAME/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api
