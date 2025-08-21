# Django + PostgreSQL/Supabase • CRUD API + 3rd‑party API + Charts

A minimal, interview‑friendly Django app you can run locally in minutes and deploy to Render/anywhere with a Postgres (or Supabase) database.

## Features
- **CRUD REST API** for `Task` (Django REST Framework)
- **3rd‑party API integration**: weather from Open‑Meteo (`/api/weather?city=Pune`) and a POST echo (`/api/echo`)
- **Simple reporting & data viz**: `/api/report` feeds **Chart.js** on the homepage
- **PostgreSQL/Supabase ready** via `DATABASE_URL`, falls back to SQLite for quick local spins

---

## Quickstart (Windows + VS Code)

1) **Clone & venv**
```powershell
git clone REPO_URL django-supabase-demo
cd django-supabase-demo

# Python 3.12 recommended
py -3.12 -m venv .venv
.\.venv\Scripts\Activate

python -m pip install --upgrade pip
pip install -r requirements.txt
```

2) **Run migrations & start**
```powershell
# Copy env
copy .env.example .env
# (keep DEBUG=1 for local dev; SQLite is used automatically if DATABASE_URL is unset)

python manage.py migrate
python manage.py runserver
```
Open http://127.0.0.1:8000

3) **Try it**
- Create a task in the UI (home page) or via API:
  - `POST /api/tasks/` with JSON `{ "title": "demo" }`
- Charts auto‑update via `/api/report`
- Weather: `GET /api/weather?city=Pune`
- Echo: `POST /api/echo` with any JSON

---

## Switch to PostgreSQL (Supabase or any Postgres)

**Supabase** (free):
- Create a project → Settings → **Database** → copy **Connection string** (URI).
- Set it in `.env` as `DATABASE_URL=postgresql://...sslmode=require`
- Apply migrations:
```powershell
python manage.py migrate
```
- (Optional) create a superuser: `python manage.py createsuperuser` then open `/admin`.

---

## Deploy on Render (fast)

1. Push to GitHub (public or private).
2. On Render: **New → Web Service → Build from repo**.
3. Runtime **Python**. Render reads `render.yaml`/`Procfile`.
4. Add env vars:
   - `DATABASE_URL` (from Supabase or Render Postgres add‑on)
   - `SECRET_KEY` (any strong string)
   - `DEBUG=0`
   - `ALLOWED_HOSTS=*`
5. Deploy. Visit the URL, load `/` and test endpoints under `/api/`.

---

## Project Structure
```
core/               # settings, urls
tasks/              # app with model, serializers, views, routes
templates/index.html# simple UI + Chart.js
static/             # static assets (optional)
```

---

## API Reference (short)
- `GET/POST /api/tasks/`
- `GET/PATCH/DELETE /api/tasks/<id>/`
- `GET /api/report/` → `{ by_status: [...], by_day: [...] }`
- `GET /api/weather?city=Pune`
- `POST /api/echo` → forwards your JSON to Postman Echo

---

## Tests (manual quick checks)
- Create 3 tasks with different statuses; confirm both charts update.
- Hit `/api/weather?city=Pune` → see coords + hourly temps.
- `DELETE` a task; charts change accordingly.

---

## Notes
- Uses `WhiteNoise` for static files in production.
- Time zone set to `Asia/Kolkata`.
- CORS open for demo simplicity; restrict in real apps.
```

