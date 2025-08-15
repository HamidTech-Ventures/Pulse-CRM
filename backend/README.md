# Project Management API (Django + DRF)

Production-grade REST API with JWT auth, role-based permissions, and PostgreSQL. Includes Docker Compose with Postgres and pgAdmin.

## Features
- Django 5 + DRF
- JWT auth (simplejwt)
- Custom `users.User` with `role` (ADMIN/CLIENT)
- Apps: `users`, `clients`, `employees`, `projects`
- CRUD endpoints for Admin; Client read-only projects via `/api/projects/my-projects/`
- Filtering, search, ordering, pagination
- CORS for React
- OpenAPI docs at `/api/docs/`

## Quickstart (Docker)
1. Copy env
```bash
cp .env.example .env
```
2. Launch services
```bash
docker compose up --build
```
3. Create superuser (new shell)
```bash
docker compose exec backend python manage.py createsuperuser --email admin@example.com
```

pgAdmin: `http://localhost:5050` (admin@local.test / admin). Add server `db:5432` with user `postgres` and password `postgres`.

## Local (without Docker)
- Ensure Postgres is running and set `DATABASE_URL` in `.env` (e.g. `postgresql://postgres:postgres@localhost:5432/app_db`).
- Create venv and install requirements: `pip install -r requirements.txt`
- Run: `python manage.py migrate && python manage.py runserver`

## Environment
- `DEBUG`, `SECRET_KEY`, `ALLOWED_HOSTS`
- `DATABASE_URL`
- `CORS_ALLOWED_ORIGINS`, `CSRF_TRUSTED_ORIGINS`

## API Overview
- Auth
  - POST `/api/auth/login/` → `{ email, password }` → `{ success, message, data:{ access_token, role } }`
  - GET `/api/auth/me/`
- Clients (Admin only for write)
  - `/api/clients/`
- Employees (Admin only for write)
  - `/api/employees/`
- Projects
  - `/api/projects/` (Admin write; all authenticated read)
  - GET `/api/projects/my-projects/` (Client read-only of assigned projects)

Responses follow:
```json
{ "success": true, "message": "...", "data": { ... } }
```

## Testing
```bash
docker compose exec backend python manage.py test
```