# 📝 Task Management API

A lightweight, performant Task Management API built with [FastAPI](https://fastapi.tiangolo.com/), [Pydantic](https://pydantic-docs.helpmanual.io/), and [SQLModel](https://sqlmodel.tiangolo.com/).

---

## 🚀 Features

* **CRUD**: Create, Read, Update, Delete tasks
* **Filtering**: Query by status (`pending`, `in_progress`, `completed`) and priority (`low`, `medium`, `high`)
* **Auto Docs**: Interactive Swagger UI & ReDoc at `/docs` and `/redoc`
* **Zero Config**: SQLite backend out-of-the-box

---

## 📦 Installation

```bash
# Clone
git clone https://github.com/OmarAnalog/task-management-api.git

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Quick Start

```bash
# Start the API server
uvicorn main:app --reload
```

Browse docs:

* Swagger UI: `http://localhost:8000/docs`
* ReDoc: `http://localhost:8000/redoc`

---

## 🔌 API Endpoints

| Method | Endpoint                     | Description                       |
| ------ | ---------------------------- | --------------------------------- |
| POST   | `/tasks/`                    | Create a new task                 |
| GET    | `/tasks/`                    | List tasks (skip, limit, filters) |
| GET    | `/tasks/{task_id}`           | Retrieve a task by **ID**         |
| PUT    | `/tasks/{task_id}`           | Update a task (partial supported) |
| DELETE | `/tasks/{task_id}`           | Delete a task                     |
| GET    | `/tasks/status/{status}`     | List tasks by **status**          |
| GET    | `/tasks/priority/{priority}` | List tasks by **priority**        |

---

## 💡 Examples (curl)

> **Create**

```bash
curl http://localhost:8000/tasks \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "Buy groceries",
    "description": "Milk, Eggs, Bread",
    "status": "pending",
    "priority": "medium"
}'
```

> **Read**

```bash
curl http://localhost:8000/tasks/1
```

> **Update**

```bash
curl http://localhost:8000/tasks/1 \
  -X PUT \
  -H 'Content-Type: application/json' \
  -d '{"status": "completed"}'
```

> **Delete**

```bash
curl http://localhost:8000/tasks/1 -X DELETE
```

> **Filter**

```bash
curl "http://localhost:8000/tasks?status=in_progress&priority=high"
```

---

## 🛠️ Configuration

All settings are in `main.py` and can be overridden via environment variables.

## 🙌 Contributing

1. Fork it
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
