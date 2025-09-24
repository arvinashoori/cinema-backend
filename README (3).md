# Sales Automation Planner

This project is a Django-based AI-powered planning system. It integrates with LLMs to generate marketing funnels and orchestration tasks, and uses Celery with Redis for task scheduling.

---

## 🚀 Setup Instructions

### 1. Clone Repository
```bash
git clone <your-development-repo-url>
cd Sales-Automation
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ⚙️ Environment Variables
Create a `.env` file in the project root:

```
DJANGO_SECRET_KEY=replace_me
DJANGO_DEBUG=True

OPENROUTER_API_KEY=sk-REPLACE_ME
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_MODEL=openai/gpt-4o-mini

---


## ⚙️ Database Setup

### Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 📡 Background Services

### Start Redis
You must have Redis installed and running on port **6379**.

On Linux/Mac:
```bash
redis-server
```

On Windows (using WSL or pre-installed service):
```bash
redis-server
```

### Start Celery Worker
Run this in a new terminal:
```bash
celery -A Sales_Automation worker -l info
```

### Start Celery Beat (for scheduled tasks)
Optional, if you plan to use scheduled runs:
```bash
celery -A Sales_Automation beat -l info
```

---

## 🛠 Development Commands

### Seed Fake Data
This will create demo `Effort`, `Brand`, and related records:
```bash
python manage.py seed_fake_data
```

### Run AI Planner
To generate plan + tasks for a given effort (example: ID 1):
```bash
python manage.py run_planner 1
```

---

## 📂 Project Structure
```
Sales_Automation/
├── planner/                 # Core planning app
│   ├── management/commands/ # Custom management commands
│   ├── models.py            # Database models
│   ├── planner_agent.py     # Main AI planner workflow
│   ├── repos.py             # Repository layer
│   ├── task.py              # Celery tasks
│   ├── views.py             # API views
├── Sales_Automation/        # Project config (settings, celery, urls)
├── db.sqlite3               # Local SQLite database
├── .env                     # Environment variables
├── requirements.txt         # Dependencies
└── README.md
```

---

## ✅ Flow Summary
1. Install dependencies  
2. Run migrations  
3. Start Redis + Celery  
4. Seed fake data (`seed_fake_data`)  
5. Run planner (`run_planner <effort_id>`)

---
