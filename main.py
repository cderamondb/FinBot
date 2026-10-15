from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from agent import FinancialAgent

app = FastAPI(title="Agente Financiero IA")

app.mount("/static", StaticFiles(directory="static"), name="static")

sessions: dict[str, FinancialAgent] = {}


class ChatRequest(BaseModel):
    session_id: str
    message: str


class ChatResponse(BaseModel):
    response: str


@app.get("/")
async def root():
    return FileResponse("static/index.html")


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    if req.session_id not in sessions:
        sessions[req.session_id] = FinancialAgent()

    agent = sessions[req.session_id]
    response = agent.chat(req.message)
    return ChatResponse(response=response)


@app.post("/reset")
async def reset(req: ChatRequest):
    if req.session_id in sessions:
        sessions[req.session_id].reset()
    return {"status": "ok"}
