from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from uuid import uuid4

from decision import decide
from conversation import ConversationContext


# ============================================================
# FASTAPI APP
# ============================================================

app = FastAPI(
    title="Shubhank Resume AI",
    description="AI-powered resume assistant",
    version="1.0.0"
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:3000",
        "https://shubhankportfolio.netlify.app"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


# ============================================================
# SESSION STORAGE
# ============================================================

conversations = {}


# ============================================================
# REQUEST MODEL
# ============================================================

class ChatRequest(BaseModel):

    message: str
    session_id: str | None = None


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/")
def home():

    return {
        "status": "online",
        "message": "Shubhank Resume AI is running"
    }


# ============================================================
# CHAT
# ============================================================

@app.post("/chat")
def chat(request: ChatRequest):

    # --------------------------------------------------------
    # CREATE SESSION ID
    # --------------------------------------------------------

    session_id = request.session_id

    if not session_id:

        session_id = str(uuid4())


    # --------------------------------------------------------
    # GET / CREATE CONVERSATION
    # --------------------------------------------------------

    if session_id not in conversations:

        conversations[session_id] = ConversationContext()


    conversation = conversations[session_id]


    # --------------------------------------------------------
    # DECISION ENGINE
    # --------------------------------------------------------

    result = decide(
        request.message,
        conversation
    )


    # --------------------------------------------------------
    # RESPONSE
    # --------------------------------------------------------

    return {

        "session_id": session_id,

        "answer": result["answer"],

        "intent": result["intent"],

        "confidence": result.get(
            "neural_confidence"
        ),

        "reason": result["reason"]
    }