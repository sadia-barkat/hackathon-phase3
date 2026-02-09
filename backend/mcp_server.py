from mcp.server.fastmcp import FastMCP
from sqlmodel import Session, select
from backend.models import Task, engine # Hum purana engine use karenge

# 1. MCP Server Initialize karein
mcp = FastMCP("Todo-Manager")

# 2. Tool: Naya Task Add Karna
@mcp.tool()
def add_task(user_id: str, title: str, description: str = None) -> dict:
    """Create a new task in the database."""
    with Session(engine) as session:
        new_task = Task(user_id=user_id, title=title, description=description)
        session.add(new_task)
        session.commit()
        session.refresh(new_task)
        return {"task_id": new_task.id, "status": "created", "title": new_task.title}

# 3. Tool: Tasks ki List Dekhna
@mcp.tool()
def list_tasks(user_id: str, status: str = "all") -> list:
    """Retrieve tasks from the list based on status (all, pending, completed)."""
    with Session(engine) as session:
        statement = select(Task).where(Task.user_id == user_id)
        
        if status == "pending":
            statement = statement.where(Task.completed == False)
        elif status == "completed":
            statement = statement.where(Task.completed == True)
            
        results = session.exec(statement).all()
        return [{"id": t.id, "title": t.title, "completed": t.completed} for t in results]

# 4. Tool: Task ko Complete karna
@mcp.tool()
def complete_task(user_id: str, task_id: int) -> dict:
    """Mark a task as complete."""
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if task and task.user_id == user_id:
            task.completed = True
            session.add(task)
            session.commit()
            return {"task_id": task.id, "status": "completed", "title": task.title}
        return {"error": "Task not found"}