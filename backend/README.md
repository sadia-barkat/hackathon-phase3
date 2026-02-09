# FastAPI Todo Application with Neon.tech PostgreSQL

A production-ready RESTful API for managing todos, built with FastAPI and PostgreSQL (Neon.tech).

## 🚀 Features

- ✅ Full CRUD operations (Create, Read, Update, Delete)
- 📊 Statistics endpoint for todo analytics
- 🔍 Filter todos by completion status
- 📄 Pagination support
- 🗄️ PostgreSQL database with SQLAlchemy ORM
- 📝 Automatic API documentation (Swagger UI)
- 🔒 CORS enabled for frontend integration
- ⚡ Fast and async with FastAPI
- 🏥 Health check endpoint

## 📋 Prerequisites

- Python 3.8+
- WSL (Windows Subsystem for Linux) or Linux environment
- PostgreSQL database (Neon.tech account)

## 🛠️ Installation & Setup

### 1. Navigate to backend directory
```bash
cd backend
```

### 2. Create virtual environment (recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On WSL/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables (Optional)
The database connection string is already configured in the code. If you want to use environment variables:

```bash
cp .env.example .env
# Edit .env with your configuration
```

## 🚀 Running the Application

### Development Mode (with auto-reload)
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Or simply:
```bash
python main.py
```

### Production Mode
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API**: http://localhost:8000
- **Swagger Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📚 API Endpoints

### Base Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint with API info |
| GET | `/health` | Health check and database status |

### Todo Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/todos` | Create a new todo |
| GET | `/todos` | Get all todos (with filtering) |
| GET | `/todos/{todo_id}` | Get a specific todo |
| PUT | `/todos/{todo_id}` | Update a todo |
| DELETE | `/todos/{todo_id}` | Delete a todo |
| PATCH | `/todos/{todo_id}/complete` | Mark todo as complete |
| GET | `/todos/stats/summary` | Get todo statistics |

## 📝 Example API Requests

### Create a Todo
```bash
curl -X POST "http://localhost:8000/todos" \
  -H "Content-Type: application/json" \
  -d '{"title": "Complete hackathon project", "completed": false}'
```

### Get All Todos
```bash
curl "http://localhost:8000/todos"
```

### Get Completed Todos Only
```bash
curl "http://localhost:8000/todos?completed=true"
```

### Update a Todo
```bash
curl -X PUT "http://localhost:8000/todos/1" \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated title", "completed": true}'
```

### Delete a Todo
```bash
curl -X DELETE "http://localhost:8000/todos/1"
```

### Mark as Complete
```bash
curl -X PATCH "http://localhost:8000/todos/1/complete"
```

### Get Statistics
```bash
curl "http://localhost:8000/todos/stats/summary"
```

## 📊 Database Schema

### Todo Table
```sql
CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT FALSE
);
```

## 🔧 Pydantic Schemas

### TodoCreate
```python
{
    "title": "string",
    "completed": false  # optional, defaults to false
}
```

### TodoUpdate
```python
{
    "title": "string",      # optional
    "completed": boolean    # optional
}
```

### TodoResponse
```python
{
    "id": 1,
    "title": "string",
    "completed": false
}
```

## 🧪 Testing the API

### Using Swagger UI (Recommended)
1. Navigate to http://localhost:8000/docs
2. Click on any endpoint
3. Click "Try it out"
4. Fill in the parameters
5. Click "Execute"

### Using curl (see examples above)

### Using Python requests
```python
import requests

# Create a todo
response = requests.post(
    "http://localhost:8000/todos",
    json={"title": "Test todo", "completed": False}
)
print(response.json())

# Get all todos
response = requests.get("http://localhost:8000/todos")
print(response.json())
```

## 📁 Project Structure

```
backend/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── .env.example        # Environment variables template
└── README.md           # This file
```

## 🔐 Security Notes

- The connection string is hardcoded for hackathon purposes
- For production, use environment variables
- Enable proper authentication/authorization
- Adjust CORS settings for production

## 🚨 Troubleshooting

### Database Connection Issues
```bash
# Test database connection
curl http://localhost:8000/health
```

### Port Already in Use
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Or use a different port
uvicorn main:app --port 8001
```

### Module Not Found
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

## 📦 Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for FastAPI
- **SQLAlchemy**: SQL toolkit and ORM
- **Psycopg2**: PostgreSQL adapter for Python
- **Pydantic**: Data validation using Python type hints

## 🎯 Next Steps

1. Add authentication (JWT tokens)
2. Add user management
3. Implement due dates and priorities
4. Add task categories/tags
5. Build a frontend (React, Vue, etc.)
6. Deploy to cloud (Vercel, Railway, etc.)

## 📞 Support

For issues or questions during the hackathon, check:
- FastAPI docs: https://fastapi.tiangolo.com/
- SQLAlchemy docs: https://docs.sqlalchemy.org/
- Neon.tech docs: https://neon.tech/docs/

## 🏆 Hackathon Tips

- Use the Swagger UI for quick testing
- Check `/health` endpoint to verify database connection
- Use `/todos/stats/summary` to show progress
- Enable auto-reload during development

Good luck with your hackathon! 🚀
