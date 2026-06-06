# SchoolApp

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)
![Status](https://img.shields.io/badge/Status-Learning%20Project-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

SchoolApp is a FastAPI-based backend project for managing student records with authentication, role-based access control, and a simple student information API. It demonstrates how a school or college system can separate access between students and teachers while keeping student profile data available through clean HTTP endpoints.

This project was built as a practical learning project to understand backend development, API design, authentication, password hashing, JWT tokens, SQLAlchemy, SQLite, and modular FastAPI routing.

## Table of Contents

- [Project Overview](#project-overview)
- [Learning Journey](#learning-journey)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [Project Structure](#project-structure)
- [Development Process](#development-process)
- [Installation Guide](#installation-guide)
- [API Documentation](#api-documentation)
- [Database Design](#database-design)
- [Security Implementation](#security-implementation)
- [Screenshots](#screenshots)
- [Key Learnings](#key-learnings)
- [Challenges and Solutions](#challenges-and-solutions)
- [Future Enhancements](#future-enhancements)
- [Performance Optimizations](#performance-optimizations)
- [Testing](#testing)
- [Deployment](#deployment)
- [Resume Impact](#resume-impact)
- [Recruiter Highlights](#recruiter-highlights)
- [Conclusion](#conclusion)

## Project Overview

SchoolApp solves a common academic management problem: schools and colleges need a secure way to register users, authenticate them, and expose different operations depending on whether the user is a student or teacher.

In the current version, the system supports:

- Student signup and login
- Password hashing with bcrypt
- JWT-based authentication
- Student-only routes for viewing student records
- Teacher-only routes for managing student data
- SQLite database storage for registered users
- JSON-based storage for sample student profile data

### Why This Project Was Built

The goal of this project was not only to build an API, but to understand the real backend concepts behind production applications:

- How API routes are organized in modules
- How user credentials should be stored securely
- How login systems issue access tokens
- How protected routes verify identity before returning data
- How role-based authorization separates permissions
- How FastAPI, SQLAlchemy, and SQLite work together

### Who Can Use It

This project is useful for:

- Students learning backend development
- Beginners building their first authenticated API
- Developers practicing FastAPI and SQLAlchemy
- Recruiters reviewing backend fundamentals
- Anyone building a small school, college, or student portal prototype

### Real-World Use Cases

- Student information portal
- College backend API prototype
- Teacher dashboard backend
- Role-based academic management system
- Authentication practice project
- Foundation for a larger school ERP system

## Learning Journey

Building this project involved moving from basic API routes to a more structured backend system.

### 1. Understanding FastAPI Routing

The first step was learning how FastAPI handles routes using `APIRouter`. Instead of keeping every endpoint in `main.py`, the project separates logic into modules:

- `auth/routes.py` for authentication
- `student/routes.py` for student-facing routes
- `teacher/routes.py` for teacher-facing routes

This helped make the project easier to read, test, and expand.

### 2. Learning Database Connectivity

The project uses SQLAlchemy to connect FastAPI with SQLite. The database setup is handled inside `database.py`, where the engine, session factory, and base model are created.

This introduced key backend concepts:

- Database connection strings
- ORM models
- Sessions
- Table creation
- Dependency injection for database access

### 3. Implementing User Registration

The signup flow required validating user input, checking whether an email already exists, hashing the password, and saving the user to the database.

The important lesson here was that raw passwords should never be stored directly. The project uses `passlib` with bcrypt to store hashed passwords.

### 4. Implementing Login With JWT

The login endpoint uses `OAuth2PasswordRequestForm`, verifies the entered password, and returns a signed JWT access token.

This introduced:

- Token-based authentication
- JWT payloads
- Expiration time
- Bearer tokens
- Protected route dependencies

### 5. Adding Role-Based Access Control

The project separates users by role. A student can access student routes, while a teacher can access teacher routes.

This is implemented through dependency functions:

- `student_only`
- `teacher_only`
- `get_current_user`

These functions decode the JWT token and decide whether the user has permission to access the route.

### 6. Working With JSON Data

Student profile details are stored in `data/student_data.json`. This made it easier to practice file-based data operations before moving everything into database tables.

The teacher routes demonstrate how an API can add, update, and remove student records from a data source.

## Features

| Feature | Beginner-Friendly Explanation | Technical Explanation | Benefit |
|---|---|---|---|
| Student Signup | New students can create an account. | `POST /auth/signup` validates input and stores a bcrypt password hash in SQLite. | Creates secure user accounts. |
| Student Login | Students can log in using email and password. | `POST /auth/login` verifies credentials and returns a JWT bearer token. | Enables authenticated API access. |
| Password Hashing | Passwords are protected before saving. | `passlib.context.CryptContext` hashes passwords using bcrypt. | Prevents plain-text password storage. |
| JWT Authentication | Logged-in users receive a token. | `python-jose` signs and decodes JWTs using HS256. | Stateless authentication for APIs. |
| Student Routes | Students can view student data. | Routes use `Depends(student_only)` for authorization. | Keeps access controlled. |
| Teacher Routes | Teachers can manage student records. | Routes use `Depends(teacher_only)` and JSON file operations. | Demonstrates admin-style permissions. |
| Modular Code Structure | Code is split into clear folders. | Separate routers are included in `main.py`. | Easier maintenance and scaling. |
| SQLite Database | Data is stored locally. | SQLAlchemy connects to `sqlite:///./school.db`. | Simple local development with no external database server. |
| Interactive API Docs | API can be tested in the browser. | FastAPI automatically exposes `/docs` and `/redoc`. | Faster debugging and learning. |

## Tech Stack

| Technology | What It Is | Why It Was Chosen | How It Is Used |
|---|---|---|---|
| Python 3.11 | General-purpose backend programming language. | Simple syntax, strong ecosystem, excellent for APIs. | Main language for the complete backend. |
| FastAPI | Modern Python web framework for APIs. | Fast, beginner-friendly, automatic docs, built-in validation. | Defines all auth, student, and teacher endpoints. |
| Uvicorn | ASGI server for Python web apps. | Recommended server for running FastAPI locally. | Runs the API during development. |
| SQLAlchemy | Python ORM and database toolkit. | Allows database tables to be represented as Python classes. | Defines the `Student` model and manages SQLite sessions. |
| SQLite | Lightweight file-based SQL database. | Easy setup for local projects and learning. | Stores registered users in `school.db`. |
| Pydantic | Data validation library. | FastAPI uses it naturally for request validation. | Defines request schemas such as `StudentSignup`. |
| Passlib | Password hashing library. | Provides secure password hashing utilities. | Hashes and verifies passwords with bcrypt. |
| bcrypt | Password hashing algorithm. | Strong standard for password storage. | Used through Passlib. |
| python-jose | JWT library for Python. | Supports signing and decoding JWT tokens. | Creates and validates access tokens. |
| python-multipart | Form data parser. | Required by FastAPI for OAuth2 form login. | Supports `OAuth2PasswordRequestForm` in login. |
| JSON | Lightweight data format. | Simple for learning file-based data workflows. | Stores sample student profile records. |

## System Architecture

The application follows a modular backend architecture:

```text
Client / API Tool
        |
        v
FastAPI Application
        |
        +-- Auth Router
        |     +-- Signup
        |     +-- Login
        |     +-- JWT creation
        |
        +-- Student Router
        |     +-- Student-only protected routes
        |     +-- Reads student profile JSON data
        |
        +-- Teacher Router
              +-- Teacher-only protected routes
              +-- Adds, updates, and removes student records
```

### Data Flow

1. A client sends a request to the FastAPI server.
2. FastAPI routes the request to the correct router.
3. If the route is protected, the JWT token is decoded.
4. The user role is checked.
5. The route either returns data, updates data, or rejects the request.
6. FastAPI sends a JSON response back to the client.

### Backend Workflow

The backend starts in `main.py`. It creates database tables with SQLAlchemy and registers each route module:

- Auth routes
- Student routes
- Teacher routes

Each route module handles one responsibility, keeping the backend organized.

### Frontend Workflow

This repository currently focuses on the backend API. A frontend can be added later using React, Streamlit, or any client that can send HTTP requests.

A typical frontend workflow would be:

1. User opens login page.
2. Frontend submits email and password to `/auth/login`.
3. Backend returns a JWT token.
4. Frontend stores the token securely.
5. Frontend sends the token in the `Authorization` header.
6. Backend returns protected student or teacher data.

### Database Workflow

The current database workflow uses SQLite for registered users:

1. `database.py` creates a database engine.
2. `models.py` defines the `students` table.
3. `main.py` creates tables automatically at startup.
4. Signup creates a new student row.
5. Login queries the student row by email.

Student profile records are currently stored in `data/student_data.json` to keep the project simple and readable.

### Authentication Workflow

```text
Signup
  -> Validate name, email, password
  -> Check duplicate email
  -> Hash password
  -> Save user in SQLite

Login
  -> Receive email and password
  -> Find user by email
  -> Verify password hash
  -> Create JWT token
  -> Return bearer token

Protected Route
  -> Read bearer token
  -> Decode JWT
  -> Check role
  -> Allow or reject request
```

### API Workflow

FastAPI handles API requests using route decorators such as:

- `@router.post()`
- `@router.get()`
- `@router.put()`
- `@router.delete()`

Protected endpoints use FastAPI dependencies to enforce authorization before executing route logic.

## Project Structure

```text
SchoolApp/
├── auth/
│   ├── __init__.py
│   ├── auth.py
│   ├── routes.py
│   └── utils.py
├── data/
│   └── student_data.json
├── student/
│   ├── __init__.py
│   └── routes.py
├── teacher/
│   ├── __init__.py
│   └── routes.py
├── database.py
├── main.py
├── models.py
├── school.db
└── README.md
```

### Important Folders

| Folder | Responsibility |
|---|---|
| `auth/` | Handles authentication, password hashing, JWT creation, and role authorization. |
| `student/` | Contains routes that students can access after authentication. |
| `teacher/` | Contains teacher-protected routes for managing student records. |
| `data/` | Stores sample student profile data in JSON format. |

### Important Files

| File | Responsibility |
|---|---|
| `main.py` | Application entry point. Creates database tables and registers routers. |
| `database.py` | Configures SQLite database connection, SQLAlchemy engine, session, and base model. |
| `models.py` | Defines the SQLAlchemy `Student` model used for authentication records. |
| `auth/routes.py` | Provides signup, login, and debug endpoints. |
| `auth/auth.py` | Contains JWT creation, token verification, and role-checking dependencies. |
| `auth/utils.py` | Provides password hashing and verification helpers. |
| `student/routes.py` | Provides student-only endpoints for reading student data. |
| `teacher/routes.py` | Provides teacher-only endpoints for creating, updating, and deleting student records. |
| `data/student_data.json` | Stores sample student profile records. |
| `school.db` | Local SQLite database file. |

## Development Process

| Step | Phase | What Was Done |
|---|---|---|
| 1 | Planning | Decided to build a school/student API with authentication and role-based access. |
| 2 | Research | Studied FastAPI routing, SQLAlchemy sessions, OAuth2 form login, JWT, and bcrypt hashing. |
| 3 | Environment Setup | Created a Python virtual environment and installed FastAPI, Uvicorn, SQLAlchemy, Passlib, and python-jose. |
| 4 | Backend Development | Built modular route files for authentication, student access, and teacher access. |
| 5 | Frontend Planning | Designed the backend so it can later support a React, Streamlit, or mobile frontend. |
| 6 | Database Integration | Added SQLite with SQLAlchemy and created the `students` table. |
| 7 | Testing | Tested endpoints manually through FastAPI Swagger UI and bearer-token authorization. |
| 8 | Deployment Planning | Prepared the project structure so it can be deployed later with environment variables and a production ASGI server. |

## Installation Guide

### Prerequisites

Install the following before running the project:

- Python 3.11 or newer
- Git
- pip
- A terminal or command prompt

### Clone Repository

```bash
git clone https://github.com/<your-username>/SchoolApp.git
cd SchoolApp
```

### Create Virtual Environment

Windows:

```bash
python -m venv myenv
myenv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### Install Dependencies

If you create a `requirements.txt`, install dependencies with:

```bash
pip install -r requirements.txt
```

Or install the main dependencies manually:

```bash
pip install fastapi uvicorn sqlalchemy pydantic email-validator passlib[bcrypt] python-jose python-multipart
```

### Configure Environment Variables

The current development version keeps the JWT secret directly in `auth/auth.py`:

```python
SECRET_KEY = "SECRET123"
```

For production, move this value into an environment variable:

```bash
SECRET_KEY=replace-with-a-strong-secret-key
```

Recommended future configuration:

```env
DATABASE_URL=sqlite:///./school.db
SECRET_KEY=replace-with-a-secure-secret
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Run Backend

```bash
uvicorn main:app --reload
```

The server will start at:

```text
http://127.0.0.1:8000
```

### Open API Documentation

FastAPI automatically generates interactive documentation:

```text
http://127.0.0.1:8000/docs
```

Alternative documentation:

```text
http://127.0.0.1:8000/redoc
```

### Verify Installation

1. Open `/docs`.
2. Run `POST /auth/signup`.
3. Run `POST /auth/login`.
4. Copy the returned access token.
5. Click **Authorize** in Swagger UI.
6. Test protected student or teacher endpoints.

## API Documentation

### Authentication Endpoints

#### POST `/auth/signup`

Registers a new student account.

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | Student name |
| `email` | string | Yes | Unique student email |
| `password` | string | Yes | Plain password sent by user and hashed before storage |

Example request:

```json
{
  "name": "Rahul Sharma",
  "email": "rahul.sharma@example.com",
  "password": "strongpassword123"
}
```

Example response:

```json
{
  "message": "Student registered successfully"
}
```

Possible errors:

| Status Code | Reason |
|---|---|
| `400` | Email already registered |
| `422` | Invalid request body or invalid email |

#### POST `/auth/login`

Authenticates a user and returns a JWT access token.

This endpoint uses OAuth2 form data, not raw JSON.

| Field | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | User email address |
| `password` | string | Yes | User password |

Example request using cURL:

```bash
curl -X POST "http://127.0.0.1:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=rahul.sharma@example.com&password=strongpassword123"
```

Example response:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

Possible errors:

| Status Code | Reason |
|---|---|
| `401` | Invalid email |
| `401` | Invalid password |

#### GET `/auth/debug`

Returns registered user emails and password hashes.

This is useful for development only and should be removed or protected before production deployment.

Example response:

```json
[
  {
    "email": "rahul.sharma@example.com",
    "hash": "$2b$12$..."
  }
]
```

### Student Endpoints

All student endpoints require a valid bearer token with the `student` role.

Authorization header:

```text
Authorization: Bearer <access_token>
```

#### GET `/student/view`

Returns all student records from the JSON data file.

Example request:

```bash
curl -X GET "http://127.0.0.1:8000/student/view" \
  -H "Authorization: Bearer <access_token>"
```

Example response:

```json
{
  "STU1001": {
    "student_id": "STU1001",
    "name": "Rahul Sharma",
    "email": "rahul.sharma@example.com",
    "course_branch": "B.Tech - Computer Science"
  }
}
```

#### GET `/student/{student_id}`

Returns a single student record.

Path parameter:

| Parameter | Type | Description |
|---|---|---|
| `student_id` | string | Student identifier such as `STU1001` |

Example request:

```bash
curl -X GET "http://127.0.0.1:8000/student/STU1001" \
  -H "Authorization: Bearer <access_token>"
```

Example response:

```json
{
  "student_id": "STU1001",
  "name": "Rahul Sharma",
  "email": "rahul.sharma@example.com",
  "phone": "+91-9876543210",
  "date_of_birth": "2002-05-14",
  "course_branch": "B.Tech - Computer Science",
  "year_semester": "3rd Year - Semester 6"
}
```

Possible errors:

| Status Code | Reason |
|---|---|
| `401` | Missing or invalid token |
| `403` | Token role is not `student` |
| `404` | Student not found |

### Teacher Endpoints

All teacher endpoints require a valid bearer token with the `teacher` role.

> Note: Signup currently creates users with the default `student` role. To test teacher routes, a teacher user must be added by updating the role in the database or by extending the signup flow to support teacher accounts.

#### POST `/teacher/student/{student_id}`

Adds or replaces a student record in `data/student_data.json`.

Path parameter:

| Parameter | Type | Description |
|---|---|---|
| `student_id` | string | Student identifier such as `STU1004` |

Request body:

```json
{
  "name": "Neha Singh",
  "email": "neha.singh@example.com",
  "course_branch": "B.Tech - Information Technology"
}
```

Example response:

```json
{
  "message": "Student added successfully"
}
```

#### PUT `/teacher/student/{student_id}`

Updates an existing student record.

Example request:

```json
{
  "name": "Neha Singh",
  "email": "neha.singh@example.com",
  "course_branch": "B.Tech - Artificial Intelligence"
}
```

Example response:

```json
{
  "message": "Student info updated successfully"
}
```

#### DELETE `/teacher/student/{student_id}`

Removes a student record.

Example response:

```json
{
  "message": "Student Removed Successfully"
}
```

Current implementation note: the delete route needs a small cleanup before production use. It deletes before checking whether the student exists and should write back using `json.dump(data, f, indent=4)`.

## Database Design

### SQLite Database

The SQLite database is stored in:

```text
school.db
```

### `students` Table

Defined in `models.py`.

| Column | Type | Constraint | Description |
|---|---|---|---|
| `id` | Integer | Primary key, indexed | Internal user ID |
| `name` | String | Nullable in current model | Student name |
| `email` | String | Unique, indexed | Login email |
| `hashed_password` | String | Nullable in current model | bcrypt password hash |
| `role` | String | Defaults to `student` | User role for authorization |

### JSON Student Profile Store

Student profile data is currently stored in:

```text
data/student_data.json
```

Example structure:

```json
{
  "STU1001": {
    "student_id": "STU1001",
    "name": "Rahul Sharma",
    "email": "rahul.sharma@example.com",
    "course_branch": "B.Tech - Computer Science"
  }
}
```

### Relationships

The current version does not define relational foreign keys. User login records are stored in SQLite, while detailed student records are stored in JSON.

A future production version should move profile data into database tables such as:

- `users`
- `students`
- `teachers`
- `courses`
- `enrollments`

## Security Implementation

| Security Area | Current Implementation | Production Recommendation |
|---|---|---|
| Authentication | JWT bearer tokens | Keep JWT and add refresh-token strategy if needed |
| Authorization | `student_only` and `teacher_only` dependencies | Add role management and admin-level controls |
| Password Encryption | bcrypt hashing through Passlib | Continue using strong hashing and password policies |
| Environment Variables | Secret key is hardcoded during development | Move `SECRET_KEY` and database config to `.env` |
| API Security | Protected endpoints require tokens | Add CORS rules, rate limiting, logging, and monitoring |
| Debugging | `/auth/debug` exposes hashes | Remove or protect debug routes before deployment |

### Authentication

Users log in with email and password. After successful verification, the API returns a JWT access token.

### Authorization

The token contains a `role` claim. Protected routes check the role before allowing access.

### Password Encryption

Passwords are hashed using bcrypt before being stored. During login, the entered password is verified against the stored hash.

### Environment Variables

Sensitive values should not be committed directly in source code. The JWT secret should be loaded from environment variables in a production-ready version.

## Screenshots

Add screenshots to a `screenshots/` folder and update the paths below.

### Home Page

```text
screenshots/home-page.png
```

### Login Page

```text
screenshots/login-page.png
```

### Dashboard

```text
screenshots/dashboard.png
```

### Results Page

```text
screenshots/results-page.png
```

### Architecture Diagram

```text
screenshots/architecture-diagram.png
```

## Key Learnings

### Technical Skills Learned

- Creating REST APIs with FastAPI
- Structuring routes with `APIRouter`
- Using SQLAlchemy models and sessions
- Creating SQLite-backed applications
- Hashing passwords with bcrypt
- Creating and validating JWT tokens
- Protecting routes with FastAPI dependencies
- Reading and writing JSON data
- Testing APIs through Swagger UI

### Problem-Solving Skills Learned

- Breaking a project into smaller modules
- Separating authentication from business logic
- Debugging login and password verification issues
- Thinking through role-based permissions
- Handling missing records and invalid user input
- Designing APIs that are easy to test manually

### Software Engineering Principles Learned

- Separation of concerns
- Modular design
- Secure password handling
- Stateless API authentication
- Dependency injection
- Clear route naming
- Incremental development

## Challenges and Solutions

| Challenge | Cause | Solution | Outcome |
|---|---|---|---|
| Storing passwords securely | Plain-text passwords are unsafe | Used Passlib with bcrypt hashing | Passwords are stored as hashes |
| Creating protected routes | Some endpoints should not be public | Added JWT bearer authentication | Only logged-in users can access protected routes |
| Separating student and teacher permissions | Different user types need different access | Added role checks with `student_only` and `teacher_only` | API supports role-based authorization |
| Managing database sessions | SQLAlchemy sessions must be opened and closed correctly | Created `get_db()` dependency | Database access is cleaner and safer |
| Handling duplicate users | Same email should not register twice | Checked existing email before creating account | Prevents duplicate login identities |
| Testing OAuth2 login | Login uses form data instead of JSON | Used FastAPI Swagger UI and form-urlencoded requests | Login works with FastAPI's OAuth2 flow |
| Managing student profile records | Full relational schema was not required for first version | Used JSON file storage for sample data | Faster learning and simpler development |
| Preparing for production | Development code contains hardcoded values | Documented environment-variable improvements | Clear path for production hardening |

## Future Enhancements

### Short-Term Improvements

- Add `requirements.txt`
- Add `.gitignore` for `myenv/`, `__pycache__/`, and local database files
- Move `SECRET_KEY` into environment variables
- Remove or protect `/auth/debug`
- Fix and simplify the teacher delete route
- Add a route to create teacher accounts safely
- Improve error messages and response consistency

### Long-Term Improvements

- Move all student profile data from JSON to SQL tables
- Add course and enrollment models
- Add admin role
- Add refresh tokens
- Add pagination and search
- Add file upload for student profile photos
- Build a React or Streamlit frontend
- Add automated test coverage with Pytest

### Enterprise-Level Improvements

- PostgreSQL database
- Alembic database migrations
- Docker containerization
- CI/CD pipeline
- Centralized logging
- API rate limiting
- Audit logs for teacher actions
- Role and permission management
- Monitoring and production observability

## Performance Optimizations

| Optimization | Why It Matters |
|---|---|
| FastAPI async-ready architecture | Provides a high-performance foundation for API development. |
| Indexed email column | Improves lookup speed during login. |
| JWT-based stateless auth | Avoids server-side session storage for each request. |
| Modular route loading | Keeps code organized as the project grows. |
| Lightweight SQLite database | Makes local development fast and simple. |

Future performance improvements:

- Replace JSON file storage with database queries
- Add pagination for large student lists
- Add database indexes for frequently queried fields
- Use connection pooling with a production database
- Cache frequently accessed public data where appropriate

## Testing

### Manual Testing

Manual testing can be done through:

```text
http://127.0.0.1:8000/docs
```

Recommended manual test flow:

1. Register a student using `/auth/signup`.
2. Log in using `/auth/login`.
3. Authorize Swagger UI with the returned bearer token.
4. Call `/student/view`.
5. Call `/student/STU1001`.
6. Create or update a teacher user role.
7. Test teacher-protected routes.

### Unit Testing

Recommended unit tests:

- Password hashing and verification
- JWT creation and decoding
- Duplicate email validation
- Role authorization helpers
- Student JSON loading

### Integration Testing

Recommended integration tests:

- Signup to login flow
- Login to protected route flow
- Invalid token rejection
- Student role blocked from teacher routes
- Teacher role blocked from student-only routes if required

## Deployment

The current version is designed for local development. Before deploying, complete the following production steps:

1. Create `requirements.txt`.
2. Move secrets into environment variables.
3. Remove development-only debug endpoints.
4. Use PostgreSQL or another production database.
5. Add database migrations with Alembic.
6. Configure CORS for the frontend domain.
7. Run the app with a production ASGI server setup.

Example production-style command:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```



## Known Implementation Notes

This is a learning project and is still evolving. Before using it in production, the following should be addressed:

- `SECRET_KEY` should be moved out of source code.
- `/auth/debug` should be removed or protected.
- Teacher account creation needs a controlled workflow.
- The delete route in `teacher/routes.py` needs cleanup.
- JSON file storage should be replaced with database tables for real production use.
- `myenv/`, `__pycache__/`, and local database files should be excluded from Git commits.

## Conclusion

SchoolApp is a practical backend project that shows how a school management API can be built with FastAPI, SQLAlchemy, SQLite, JWT authentication, password hashing, and role-based access control.

The project covers important backend fundamentals while leaving clear space for future improvements such as a frontend dashboard, production database, automated tests, deployment, and a more complete academic management workflow.
