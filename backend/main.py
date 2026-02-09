from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from backend.models import Task, Conversation, Message, engine
from backend.agent import run_conversation # Jo humne Step 4 mein banaya
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
@app.get("/")
def home():
    return {"status": "Server is running!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Sab ko ijazat de di
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database Tables Banane ke liye (Startup par)
#@app.on_event("startup")
#def on_startup():
   # from sqlmodel import SQLModel
    #SQLModel.metadata.create_all(engine)

# MAIN CHAT ENDPOINT
@app.post("/api/{user_id}/chat")
async def chat_endpoint(user_id: str, message: str, conversation_id: int = None):
    with Session(engine) as session:
        # 1. Conversation dhoondo ya nayi banao
        if conversation_id:
            db_conv = session.get(Conversation, conversation_id)
        else:
            db_conv = Conversation(user_id=user_id)
            session.add(db_conv)
            session.commit()
            session.refresh(db_conv)

        # 2. Purani History nikaalo
        history_msgs = session.exec(
            select(Message).where(Message.conversation_id == db_conv.id)
        ).all()
        
        # Format history for OpenAI
        history = [{"role": m.role, "content": m.content} for m in history_msgs]

        # 3. User message DB mein save karo
        user_msg = Message(conversation_id=db_conv.id, user_id=user_id, role="user", content=message)
        session.add(user_msg)
        
        # 4. Agent se Jawab mango (Step 4 wali logic)
        ai_response = run_conversation(user_id, message, history)
        
        # 5. AI ka jawab DB mein save karo
        assistant_msg = Message(conversation_id=db_conv.id, user_id=user_id, role="assistant", content=ai_response)
        session.add(assistant_msg)
        
        session.commit()

        return {
            "conversation_id": db_conv.id,
            "response": ai_response
        }