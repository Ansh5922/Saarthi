from fastapi import APIRouter
from pydantic import BaseModel

from services.llm_service import generate_response
from services.intent_service import classify_intent

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

SYSTEM_PROMPT = """
You are Saarthi, a productivity assistant.

Your job:
- Analyze user's productivity issues
- Give clear, actionable suggestions
- Be concise and practical
"""

@router.post("/chat")
def chat(req: ChatRequest):
    user_message = req.message

    # STEP 1: Intent Classification
    intent = classify_intent(user_message)

    # STEP 2: Data Mapping
    context = "" # Placeholder for any additional context we might want to add based on intent
    
     
    full_prompt = f"""
{SYSTEM_PROMPT}

Intent: {intent}

Context: {context}

User: {req.message}
"""

    response = generate_response(full_prompt)

    return {
        "intent": intent,
        "response": response
    }