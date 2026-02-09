# Todo App: Spec-Driven Development

This project is a 5-phase evolution of a Todo application, starting from a Console App to a Cloud-Native AI Chatbot.

## Build & Setup Commands
- **Backend (FastAPI):** `cd backend && uv run main.py`
- **Frontend (Next.js):** `cd frontend && npm run dev`
- **Environment:** Use Python 3.13+ and Node.js 20+

## Test Commands
- **Backend Tests:** `pytest` (Run from backend folder)
- **Frontend Tests:** `npm test` (Run from frontend folder)
- **Linting:** `ruff check .` (Python) / `npm run lint` (JS)

## Code Style & Guidelines
- **Architecture:** Strictly follow Spec-Driven Development. Never write code before updating specs in `/specs`.
- **Backend:** - Use Python with **FastAPI** and **SQLModel**.
  - Follow Type Hinting and PEP 8 standards.
- **Frontend:** - Use **Next.js** (App Router) with **Tailwind CSS**.
  - Use TypeScript for all components.
- **Naming Conventions:** - Python: `snake_case` for functions/variables.
  - TypeScript: `camelCase` for variables, `PascalCase` for components.
- **Database:** Use **Neon DB** (PostgreSQL) via SQLModel.

## Spec-Driven Workflow
1. Update relevant spec in `specs/`.
2. Reference the spec file using `@` when prompting Claude Code.
3. Verify implementation matches the spec exactly.