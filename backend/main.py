from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import matplotlib
matplotlib.use('Agg') 



load_dotenv()

app = FastAPI()






# ✅ CORS (important for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = os.getenv("OPENROUTER_API_KEY")

class ChatRequest(BaseModel):
    prompt: str
    session_id: str

@app.get("/")
def home():
    return {"message": "Backend is running 🚀"}

# Dictionary to store conversation history per session
sessions = {}

@app.post("/chat")
def chat(request: ChatRequest):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    system_prompt = """
You are an experienced civil engineer and home design consultant in India.

Your goal is NOT just to give data, but to guide the user like a friendly expert.

STYLE:
- Be slightly conversational and engaging (not robotic)
- Add short explanations and reasoning
- Make the user feel excited about their home
- Use simple but professional language

RULES:
- Always use INR (₹)
- Be realistic with Indian construction costs
- Respect plot size strictly
- Suggest smart and aesthetic ideas

FORMAT YOUR RESPONSE LIKE THIS:

🏠 Overview:
- Start with a short engaging summary of the house idea

📐 Floor Plan:
- Explain layout with logic (why this design works)

💰 Estimated Cost:
- Give range + reasoning

🧱 Materials Breakdown:
- Give approximate numbers but explain briefly

🎨 Aesthetic & Lifestyle Ideas:
- Interior + Indian cultural elements (pooja, vastu, etc.)

💡 Smart Optimizations:
- Specific practical cost-saving ideas

🚀 Future Potential:
- Expansion, rental, terrace, etc.

Keep response attractive, readable, and helpful — not just numbers.
"""

    session_id = request.session_id
    if session_id not in sessions:
        sessions[session_id] = []

    sessions[session_id].append({
        "role": "user",
        "content": request.prompt
    })

    # Limit history to last 10 messages to avoid token bloat
    recent_history = sessions[session_id][-10:]

    data = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {"role": "system", "content": system_prompt},
            *recent_history
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        ai_reply = result["choices"][0]["message"]["content"]
        
        sessions[session_id].append({
            "role": "assistant",
            "content": ai_reply
        })

        return {"response": ai_reply}
    except Exception as e:
        return {"error": str(e), "response": "I'm having trouble connecting to my brain right now. Please try again later!"}