# Healthcare Backend API

A RESTful healthcare backend built with Django, Django REST Framework (DRF), and PostgreSQL. It provides JWT-based authentication, patient management, doctor management, and patient–doctor assignment APIs.

## Features

- User registration and login using JWT authentication
- Patient CRUD operations with user ownership protection
- Doctor CRUD operations
- Patient–doctor assignment and mapping management
- PostgreSQL database integration using Django ORM
- Request validation and error handling
- Environment-based configuration for sensitive settings

## Technology Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Simple JWT
- `python-dotenv`

## Project Structure

```text
healthcare-backend-api/
├── api/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   └── views.py
├── config/
│   ├── settings.py
│   └── urls.py
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Prerequisites

Install the following before running the project:

- Python 3.10 or newer
- PostgreSQL
- Git
- pip

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Sabir-Qadar/healthcare-backend-api.git
cd healthcare-backend-api
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, consult the Python virtual environment documentation or use Command Prompt activation instead.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the PostgreSQL database

Open PostgreSQL using your preferred PostgreSQL client and create the database:

```sql
CREATE DATABASE healthcare_db;
```

If the database already exists, do not create it again.

### 5. Configure environment variables

Copy `.env.example` to `.env` in the project root.

**Windows PowerShell:**

```powershell
Copy-Item .env.example .env
```

Edit `.env` and provide your own values:

```env
SECRET_KEY=your-generated-django-secret-key
DEBUG=True
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
```

Replace the placeholder secret key and database password with your actual local values. Do not commit `.env` or expose its secrets publicly.

For production, use `DEBUG=False` and configure a secure secret key and appropriate allowed hosts.

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

`http://127.0.0.1:8000/`

## Authentication

Except for registration and login, the API endpoints require a valid JWT access token.

Include the token in the request header:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

Access tokens expire. Log in again or use the refresh endpoint when appropriate.

## API Endpoints

### 1. Authentication APIs

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| POST | `/api/auth/register/` | Register a user | Not required |
| POST | `/api/auth/login/` | Obtain JWT tokens | Not required |
| POST | `/api/auth/token/refresh/` | Refresh an access token | Refresh token required |

**Register a user**

`POST /api/auth/register/`

```json
{
  "first_name": "Test",
  "last_name": "User",
  "email": "user@example.com",
  "password": "StrongPassword123"
}
```

**Log in**

`POST /api/auth/login/`

```json
{
  "email": "user@example.com",
  "password": "StrongPassword123"
}
```

A successful login returns an access token and a refresh token.

### 2. Patient Management APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/patients/` | Create a patient |
| GET | `/api/patients/` | List your patients |
| GET | `/api/patients/{id}/` | Retrieve a patient |
| PUT | `/api/patients/{id}/` | Update a patient |
| PATCH | `/api/patients/{id}/` | Partially update a patient |
| DELETE | `/api/patients/{id}/` | Delete a patient |

All patient endpoints require authentication. Users can access only patient records they own.

**Create a patient**

`POST /api/patients/`

```json
{
  "name": "Test Patient",
  "age": 25,
  "gender": "Male",
  "address": "Ranchi, Jharkhand"
}
```

### 3. Doctor Management APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/doctors/` | Create a doctor |
| GET | `/api/doctors/` | List all doctors |
| GET | `/api/doctors/{id}/` | Retrieve a doctor |
| PUT | `/api/doctors/{id}/` | Update a doctor |
| PATCH | `/api/doctors/{id}/` | Partially update a doctor |
| DELETE | `/api/doctors/{id}/` | Delete a doctor |

All doctor endpoints require authentication.

**Create a doctor**

`POST /api/doctors/`

```json
{
  "name": "Dr. Test",
  "specialization": "General Medicine",
  "email": "doctor@example.com",
  "phone": "9876543210"
}
```

### 4. Patient–Doctor Mapping APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/mappings/` | Assign a doctor to a patient |
| GET | `/api/mappings/` | List your patient–doctor mappings |
| GET | `/api/mappings/{patient_id}/` | List mappings for a patient |
| DELETE | `/api/mappings/{id}/` | Delete a mapping |

All mapping endpoints require authentication. A user can create or access mappings only for patients they own.

**Assign a doctor**

`POST /api/mappings/`

```json
{
  "patient": 1,
  "doctor": 1
}
```

Replace the IDs with existing patient and doctor IDs.

**Important URL behavior:** The assignment uses the same URL pattern for retrieving mappings by patient ID and deleting mappings by mapping ID. The implementation distinguishes the operations by HTTP method: `GET` interprets the ID as a patient ID, while `DELETE` interprets it as a mapping ID.

## Testing

Use Postman, HTTPie, or another HTTP client to test the APIs.

Recommended checks:

- Successful user registration and login
- Access-token authentication
- Patient CRUD and ownership restrictions
- Doctor CRUD
- Creating and listing patient–doctor mappings
- Retrieving mappings for a specific patient
- Deleting a mapping
- Invalid input and nonexistent resource handling
- Rejection of unauthenticated requests

## Django Checks

Run the following commands to verify the project configuration and database migrations:

```bash
python manage.py check
python manage.py makemigrations --check
python manage.py migrate --check
```

## Security

- Sensitive configuration is stored in environment variables.
- `.env` must remain excluded from version control.
- JWT authentication protects API endpoints.
- Patient records and related mappings are restricted by patient ownership.
- Production deployments should disable debug mode and use secure configuration.

## Repository

GitHub: https://github.com/Sabir-Qadar/healthcare-backend-api

## Author

Sabir Qadar

GitHub: https://github.com/Sabir-Qadar