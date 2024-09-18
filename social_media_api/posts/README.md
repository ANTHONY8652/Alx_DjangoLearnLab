## Posts and Comments API

### Posts

- **List Posts**: `GET /api/posts/`
- **Create Post**: `POST /api/posts/`
  - **Fields**: `title`, `content`
- **Retrieve Post**: `GET /api/posts/{id}/`
- **Update Post**: `PUT /api/posts/{id}/`
  - **Fields**: `title`, `content`
- **Delete Post**: `DELETE /api/posts/{id}/`

### Comments

- **List Comments**: `GET /api/comments/`
- **Create Comment**: `POST /api/comments/`
  - **Fields**: `post`, `content`
- **Retrieve Comment**: `GET /api/comments/{id}/`
- **Update Comment**: `PUT /api/comments/{id}/`
  - **Fields**: `content`
- **Delete Comment**: `DELETE /api/comments/{id}/`
