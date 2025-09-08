# Django REST API Example

This project provides RESTful APIs for user registration, login (JWT authentication), and candidate creation using Django and Django REST Framework.

## Features

- **User Registration** (`/register/`)
- **User Login** (`/login/`)
- **Candidate Creation** (`/candidates/`)
- JWT authentication for secure API access

## Setup

1. **Clone the repository**
2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    pip install djangorestframework djangorestframework-simplejwt
    ```
3. **Apply migrations**
    ```bash
    python manage.py migrate
    ```
4. **Run the server**
    ```bash
    python manage.py runserver
    ```

## API Usage

### 1. Register a User

```bash
curl -X POST http://localhost:8000/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "yourpassword"
  }'
```

**Response:**
```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>",
  "user_id": 1
}
```

### 2. Login

```bash
curl -X POST http://localhost:8000/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "yourpassword"
  }'
```

**Response:**
```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>",
  "user_id": 1
}
```

### 3. Create Candidate

```bash
curl -X POST http://localhost:8000/candidates/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <access_token>" \
  -d '{
    "candidate": 1,
    "dob": "1990-01-01",
    "gender": "female",
    "address": "123 Main St",
    "resume_url": "https://example.com/resume.pdf",
    "experience": 5,
    "skills": ["Python", "Django"],
    "education": "B.Tech"
  }'
```

**Note:**  
- Replace `<access_token>` with the token received from login/register.
- Replace `candidate` value (`1`) with the actual user ID.

## Security

- All sensitive endpoints require JWT authentication.
- Always use HTTPS in production.
