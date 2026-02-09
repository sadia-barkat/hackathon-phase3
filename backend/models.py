import os
from datetime import datetime
from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship, create_engine # create_engine add kiya

# --- DATABASE CONNECTION START ---
DATABASE_URL = "YOUR_NEON_DATABASE_URL_HERE" 
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
engine = create_engine(
    DATABASE_URL, 
    connect_args={"sslmode": "require"}, # Yeh extra security connection speed barhati hai
    pool_pre_ping=True # Yeh check karta hai ke connection zinda hai ya nahi
    )
# --- DATABASE CONNECTION END ---

# 1. TASK MODEL
class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(index=True)
    title: str
    description: Optional[str] = None
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

# 2. CONVERSATION MODEL
class Conversation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    messages: List["Message"] = Relationship(back_populates="conversation")

# 3. MESSAGE MODEL
class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    conversation_id: int = Field(foreign_key="conversation.id")
    user_id: str
    role: str  # 'user' or 'assistant'
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    conversation: Optional[Conversation] = Relationship(back_populates="messages")