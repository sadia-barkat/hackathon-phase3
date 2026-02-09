from openai import OpenAI
from backend.mcp_server import mcp # Hamare banaye hue tools
import os

# OpenAI client initialize karein
# Note: Apni API Key environment variable mein set karein
client = OpenAI(api_key="YOUR_OPENAI_API_KEY_HERE")

SYSTEM_PROMPT = """
You are a helpful Todo AI Assistant. 
You can manage tasks using the provided MCP tools.
When a user asks to add, list, complete, or delete tasks, use the appropriate tool.
Always confirm your actions in a friendly way.
If a user's intent is unclear, ask for clarification.
"""

def run_conversation(user_id: str, user_message: str, history: list):
    # 1. Message array banayein (History + New Message)
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(history)
    messages.append({"role": "user", "content": user_message})

    # 2. AI ko tools ke saath call karein
    # Note: OpenAI Agents SDK ya simple Chat Completions with Tools use ho raha hai
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=mcp.get_tools_spec(), # MCP se tools ki list le raha hai
        tool_choice="auto"
    )

    return response