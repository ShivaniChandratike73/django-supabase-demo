### Django + PostgreSQL/Supabase • CRUD API + 3rd‑party API + Charts

This project is a lightweight Django web application that demonstrates how to build a clean and simple full-stack setup with Django REST Framework, PostgreSQL (or Supabase), and a touch of data visualization using Chart.js. It’s designed to be easy to run locally in just a few minutes, and it can also be deployed smoothly to platforms like Render. The app focuses on three things: a basic CRUD API for managing tasks, an integration with a third-party weather API, and a small dashboard that visualizes task data.

Features
**CRUD REST APIs** for a `Task` model (Django REST Framework)
- **Third-party API integration** (Open-Meteo geocoding + forecast) and a POST echo
- **Reporting + data visualization** (Chart.js) driven from real DB aggregates
- **Deployable** on Render with PostgreSQL/Supabase
---

### Live Demo / Repo

- **Live URL:** https://django-supabase-demo.onrender.com
---

### What’s inside

- Home page with a minimal UI (no build tools)  
  → create tasks, mark them done, delete them, view a weather call, and see two charts update.
- REST endpoints under `/api/*` used by the page and testable via cURL/Postman.
- Reporting endpoint (`/api/report/`) that powers the charts:
  - **Tasks by status** (todo/doing/done)
  - **Tasks per day** (created_at grouped by day)
---

### Tech Stack

- **Python 3.12**, **Django 5**, **Django REST Framework**
- **PostgreSQL** (works great with **Supabase**); local dev falls back to **SQLite**
- **Chart.js** for client-side charts
- **WhiteNoise** for static files in production
- **Render** ready (Procfile + `render.yaml`)
---

### Quickstart (Windows / VS Code)

```powershell
# 1) Clone
git clone https://github.com/<you>/django-supabase-demo.git
cd django-supabase-demo

# 2) Virtual env
py -3.12 -m venv .venv
.\.venv\Scripts\Activate

# 3) Install
python -m pip install --upgrade pip
pip install -r requirements.txt

# 4) Local dev env (uses SQLite if DATABASE_URL is empty)
copy .env.example .env

# 5) Migrate & run
python manage.py migrate
python manage.py runserver

Open http://127.0.0.1:8000
If PowerShell blocks activation, run once per session:
Set-ExecutionPolicy -Scope Process Bypass; .\.venv\Scripts\Activate
```
---

### Switch to PostgreSQL (Supabase)

1. Create a Supabase project → Settings → Database → set/reset the DB password.
2. Copy connection details for the Session Pooler (IPv4-friendly).
3. URL-encode your password if it has special characters:
 
python -c "import urllib.parse; print(urllib.parse.quote_plus('RawP@ss?word'))"


4. Edit .env and set:
```powershell
SECRET_KEY=zd-ik1cL8V6dId6fURXVNn6hNHEqvMKVWY0DvoNlWI93_Sl3YYnA7jkzlGKQ6VIrb_E
DATABASE_URL=postgresql://postgres.obqwatszmqegphdjvaem:sH!V@N!9cH@NDR@T!KE@aws-1-ap-south-1.pooler.supabase.com:5432/postgres?sslmode=require
DEBUG=1
ALLOWED_HOSTS=localhost,127.0.0.1
```

5. Apply migrations on Supabase:
python manage.py migrate
---

### Deploy (Render)

- Connect repo → New Web Service (Python).
- Env vars: DATABASE_URL, SECRET_KEY, DEBUG=0, ALLOWED_HOSTS=*.
- Included:
    render.yaml → builds and collects static.
    Procfile → runs gunicorn.

After deploy:

/ UI
/api/tasks/, /api/report/, /api/weather?city=Pune
---

### Troubleshooting

Venv won’t activate (PowerShell):
Set-ExecutionPolicy -Scope Process Bypass; .\.venv\Scripts\Activate

“password authentication failed”:
Use Session Pooler, correct username, and URL-encoded password; end with ?sslmode=require.

Static warning:
mkdir static (harmless locally).

### What the charts show

Tasks by Status: counts of todo/doing/done.

Tasks per Day: number of tasks created each day.
Source: /api/report/.
