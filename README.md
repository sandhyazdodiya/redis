# Django Project - Job Portal API

This project is a Django REST API for a job portal, supporting user registration, login, and CRUD operations for candidates, companies, jobs, applications, feedback, offers, and activity logs.

## Setup

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd django_project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

4. **Run the server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication

- **Register:**  
  `POST /register/`  
  **Body:**  
  ```json
  {
    "username": "yourusername",
    "password": "yourpassword"
  }
  ```

- **Login:**  
  `POST /login/`  
  **Body:**  
  ```json
  {
    "username": "yourusername",
    "password": "yourpassword"
  }
  ```

### Candidate CRUD

- **Create:**  
  `POST /candidates/`  
  **Body:**  
  ```json
  {
    "field1": "value1",
    "field2": "value2"
  }
  ```

- **Read All:**  
  `GET /candidates/`

- **Read One:**  
  `GET /candidates/<id>/`

- **Update:**  
  `PUT /candidates/<id>/`  
  **Body:**  
  ```json
  {
    "field1": "newvalue1",
    "field2": "newvalue2"
  }
  ```

- **Partial Update:**  
  `PATCH /candidates/<id>/`  
  **Body:**  
  ```json
  {
    "field1": "partialvalue"
  }
  ```

- **Delete:**  
  `DELETE /candidates/<id>/`

### Other Models

Similar CRUD endpoints exist for:
- `/users/`
- `/candidate-educations/`
- `/companies/`
- `/jobs/`
- `/job-applications/`
- `/application-feedbacks/`
- `/offers/`
- `/activity-logs/`

## Example Curl Commands

**Register**
```bash
curl -X POST http://localhost:8000/register/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "testpass123"}'
```

**Login**
```bash
curl -X POST http://localhost:8000/login/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "testpass123"}'
```

**Create Candidate**
```bash
curl -X POST http://localhost:8000/candidates/ \
     -H "Content-Type: application/json" \
     -d '{
    "candidate": 16,
    "dob": "1990-01-01",
    "gender": "female",
    "address": "123 Main St",
    "resume_url": "https://example.com/resume.pdf",
    "experience": 5,
    "skills": ["Python", "Django"],
    "education": "B.Tech"
  }'
```

**Get All Candidates**
```bash
curl http://localhost:8000/candidates/
```

**Get Candidate by ID**
```bash
curl http://localhost:8000/candidates/1/
```

**Update Candidate**
```bash
curl -X PUT http://localhost:8000/candidates/1/ \
     -H "Content-Type: application/json" \
     -d '{"field1": "newvalue1", "field2": "newvalue2"}'
```

**Delete Candidate**
```bash
curl -X