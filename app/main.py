from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define request model
class UserInput(BaseModel):
    message: str

# Simple chatbot logic
def chatbot_response(user_message):
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great! What about you?",
        "bye": "Goodbye! Have a nice day.",
    }
    return responses.get(user_message.lower(), "I'm not sure how to respond to that.")

# API endpoint for chatbot
@app.post("/chat")
def chat(user_input: UserInput):
    response = chatbot_response(user_input.message)
    return {"response": response}
