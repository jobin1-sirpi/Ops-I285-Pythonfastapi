from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

# Serve static files (for CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

class UserInput(BaseModel):
    message: str

# Custom chatbot logic
def chatbot_response(user_message):
    user_message = user_message.lower()

    responses = {
        "hi": "How can I help you?",
        "what is my name": "Your name is Jobin AJ.",
        "tell me about sirpi": """As a Bangalore-based data science company, our goal is to process your data in the most meaningful way through our rich network of research partners and domain experts. 
        Engaged in the areas of data science, data visualization, conversational chatbots, engineering research, turnkey reporting solutions, machine learning & AI programming, we aim to offer optimal solutions to your ever-evolving business needs by using data science to solve problems and process bottlenecks.
        
        We handhold you through the entire process with our highly customizable business solutions, excellent customer service & support, availability, and a limitless mindset.""",
        "hello": "Hi there! How can I assist you?",
        "how are you": "I'm an AI bot! I'm always doing great 😊",
        "bye": "Goodbye! Have a great day! 👋"
    }

    return responses.get(user_message, "I'm not sure how to respond to that.")

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
