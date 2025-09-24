# 🚀 Marketing AI Planner

An AI-powered orchestration system for marketing campaign planning, built with **Django**, **LangGraph**, **Celery**, and **Redis**.

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone <your-repo-url>
cd <your-project-folder>
pip install -r requirements.txt
```

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

REDIS_URL=redis://localhost:6379/0
CELERY_BROKER_URL=${REDIS_URL}
CELERY_RESULT_BACKEND=${REDIS_URL}
```

---

## 🗄️ Database Setup

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## ⚡ Running Celery & Redis

Start Redis (must be installed locally):

```bash
redis-server
```

Run Celery worker:

```bash
celery -A your_project_name worker -l info
```

Run Celery beat (for scheduled tasks):

```bash
celery -A your_project_name beat -l info
```

---

## 🌱 Seed Fake Data

To populate the database with fake data for testing:

```bash
python manage.py seed_fake_data
```

---

## 🧠 Run the Planner

Generate a marketing plan for a given Effort:

```bash
python manage.py run_planner <effort_id>
```

Example:

```bash
python manage.py run_planner 1
```

---

## ✅ Features

- Phase 1: Generates a **main plan** and **funnel structure**.  
- Phase 2: Orchestrates **detailed tasks** (with scheduling, dependencies, and priorities).  
- Integrated with **Celery** for async execution.  
- Uses **Redis** for task queue & result backend.  

---

## 🛠️ Tech Stack

- **Django** – Web framework  
- **LangGraph** – AI orchestration  
- **Celery + Redis** – Task scheduling  
- **OpenRouter / OpenAI** – LLM integration  

---

## 🤝 Contributing

1. Fork the repository  
2. Create your feature branch: `git checkout -b feature/my-feature`  
3. Commit changes: `git commit -m 'Add new feature'`  
4. Push branch: `git push origin feature/my-feature`  
5. Open a Pull Request 🚀  

---

## 📄 License

MIT License – free to use and modify.
