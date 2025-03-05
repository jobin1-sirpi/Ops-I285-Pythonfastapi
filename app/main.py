from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import json

app = FastAPI()

# Serve static files (for CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

class UserInput(BaseModel):
    message: str

# Simple chatbot logic
def chatbot_response(user_message):
    responses = {
        "hello": "Hi there! How can I assist you?",
        "how are you": "I'm an AI bot! I'm always doing great 😊",
        "bye": "Goodbye! Have a great day! 👋",
    }
    return responses.get(user_message.lower(), "I'm not sure how to respond to that.")

# API endpoint for chatbot
@app.post("/chat")
def chat(user_input: UserInput):
    response = chatbot_response(user_input.message)
    return {"response": response}

# Serve HTML Page
@app.get("/", response_class=HTMLResponse)
def serve_chat():
    with open("templates/index.html", "r") as f:
        return f.read()
