from services.llm_service import generate_response

INTENTS = [
    "productivity_analysis",
    "backlog_management",
    "task_planning",
    "consistency_improvement",
    "general_advice"
]

def classify_intent(user_query: str) -> str:
    prompt = f"""
You are an intent classification system.

Classify the user query into ONE of the following intents:
{', '.join(INTENTS)}

Rules:
- Output ONLY the intent name
- Do not explain anything

User Query: {user_query}
"""
    response = generate_response(prompt)

    return response.strip().lower()