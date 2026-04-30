from fastapi import APIRouter
from pydantic import BaseModel
from services.llm_service import generate_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

SYSTEM_PROMPT = """
You are Saarthi, a productivity assistant.

Your job:
- Analyze user's productivity issues
- Give clear, actionable suggestions
- Be concise and practical

Focus on:
- task completion
- procrastination
- consistency
"""

@router.post("/chat")
def chat(req: ChatRequest):
    full_prompt = f"""
{SYSTEM_PROMPT}

User: {req.message}
"""

    response = generate_response(full_prompt)

    return {
        "user_input": req.message,
        "response": response
    }