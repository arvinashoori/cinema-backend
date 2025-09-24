# SalesAutomation (Marketing AI)

Lightweight marketing & sales orchestration platform using **Django + Celery + LLM agents (OpenRouter)**.  
This README explains how to set up a local dev environment, run the services, seed fake data, and test the planner/agents.

---

## 🚀 Overview
- Django app(s) live under `Sales_Automation/`.
- Agents use an LLM (OpenRouter/OpenAI-compatible) to generate plans and orchestration tasks.
- Celery is used to enqueue and run agent tasks (Redis as broker & backend).
- A management command `run_planner` invokes the planner for an Effort.
- Command `seed_fake_data` populates dev fixtures.

---

## ⚙️ Environment Variables
Create a `.env` file in the project root:

```
DJANGO_SECRET_KEY=replace_me
DJANGO_DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3

OPENROUTER_API_KEY=sk-REPLACE_ME
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_MODEL=openai/gpt-4o-mini

# Celery + Redis
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

# For testing without Redis
CELERY_TASK_ALWAYS_EAGER=False
```

---

## 🛠 Installation

### macOS / Linux
```bash
git clone <repo-url> project
cd project

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

cp .env.example .env   # edit with your keys

python manage.py migrate
python manage.py seed_fake_data
python manage.py runserver
```

### Windows (PowerShell)
```powershell
git clone <repo-url> project
cd project

python -m venv .venv
.venv\Scripts\Activate.ps1

pip install -r requirements.txt

copy .env.example .env   # edit with your keys

python manage.py migrate
python manage.py seed_fake_data
python manage.py runserver
```

---

## 📦 Redis & Celery

### Start Redis (Docker)
```bash
docker run -d --name redis-local -p 6379:6379 redis:7
```

### Start Celery worker
```bash
celery -A Sales_Automation worker -l info
```

### Start Celery Beat (for scheduled tasks)
```bash
celery -A Sales_Automation beat -l info
```

💡 If Redis isn’t available, set `CELERY_TASK_ALWAYS_EAGER=True` in `.env` to run tasks synchronously.

---

## 📊 Running the Planner

```bash
python manage.py run_planner <effort_id>
```

This will:
1. Run **Phase 1** (plan generation via LLM).
2. Persist Plan, Funnel & Stage records.
3. Run **Phase 2** (orchestration).
4. Persist PlanTask, FunnelTask, FunnelStageTask.
5. Optionally enqueue Celery tasks.

Or from Django shell:
```python
from efforts.agents.planner import run_planner_agent
run_planner_agent(1)
```

---

## 🌱 Seeding Fake Data
Populate dev models with fake data:

```bash
python manage.py seed_fake_data
```

Or manually:
```python
python manage.py shell
>>> from efforts.models import Effort, BrandProfile
>>> b = BrandProfile.objects.create(name="Acme")
>>> Effort.objects.create(name="Test Effort", brand=b)
```

---

## 🧪 Tests
```bash
python manage.py test
```
Or with `pytest`:
```bash
pytest
```

---

## 🛡 Debugging
- **Phase 2 empty tasks** → check `Raw Phase 2 LLM output` logs and validation in planner.
- **Redis connection refused** → start Redis or set `CELERY_TASK_ALWAYS_EAGER=True`.
- **LLM errors** → ensure `OPENROUTER_API_KEY` and `OPENROUTER_BASE_URL` are correct.

---

## 📚 Deployment Notes
- Replace SQLite with Postgres in production.
- Use Docker or systemd for Celery workers & Beat.
- Keep secrets in environment variables (never in repo).
- Enable HTTPS, secure cookies, and proper CORS policies.

---

## 🔑 Useful Commands
```bash
# run dev server
python manage.py runserver

# run planner
python manage.py run_planner <effort_id>

# seed fake data
python manage.py seed_fake_data

# celery worker
celery -A Sales_Automation worker -l info

# celery beat
celery -A Sales_Automation beat -l info

# run tests
python manage.py test
```
