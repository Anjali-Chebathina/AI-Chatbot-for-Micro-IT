from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.core.utils import AvailableEndpoints
import asyncio
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from typing import Optional
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(title="Internship FAQ Chatbot API")

# Mount static files for web interface
app.mount("/static", StaticFiles(directory="static"), name="static")

class Message(BaseModel):
    sender: str
    message: str

# Load the trained model
async def load_agent():
    interpreter = RasaNLUInterpreter("./models/nlu")
    endpoints = AvailableEndpoints.read_endpoints("./endpoints.yml")
    agent = Agent.load("./models", interpreter=interpreter, action_endpoint=endpoints.action)
    return agent

# API endpoint for chat
@app.post("/chat")
async def chat(message: Message):
    agent = await load_agent()
    responses = await agent.handle_text(message.message, sender_id=message.sender)
    return {"responses": responses}

# Web interface route
@app.get("/")
async def web_interface():
    return {"message": "Web interface would be served here"}

if __name__ == "__main__":
    # Create SQLite database for logging
    import sqlite3
    conn = sqlite3.connect('question_logs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS questions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id TEXT,
                  question TEXT,
                  intent TEXT,
                  timestamp DATETIME,
                  response_quality INTEGER)''')
    conn.close()
    
    # Start the server
    uvicorn.run(app, host="0.0.0.0", port=8000)#For WhatsApp/Twilio Integration:
from fastapi import Request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# Twilio credentials
TWILIO_ACCOUNT_SID = "your_account_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_number"

@app.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    form_data = await request.form()
    user_message = form_data.get('Body')
    user_number = form_data.get('From')
    
    agent = await load_agent()
    responses = await agent.handle_text(user_message, sender_id=user_number)
    
    twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for response in responses:
        if response.get('text'):
            twilio_client.messages.create(
                body=response['text'],
                from_=TWILIO_PHONE_NUMBER,
                to=user_number
            )
    
    return {"status": "success"}
#For Telegram Integration:
import requests

TELEGRAM_TOKEN = "your_telegram_token"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

@app.post("/telegram")
async def telegram_webhook(request: Request):
    update = await request.json()
    message = update.get('message', {})
    chat_id = message.get('chat', {}).get('id')
    user_message = message.get('text')
    
    if user_message:
        agent = await load_agent()
        responses = await agent.handle_text(user_message, sender_id=str(chat_id))
        
        for response in responses:
            if response.get('text'):
                requests.post(
                    f"{TELEGRAM_API_URL}/sendMessage",
                    json={
                        "chat_id": chat_id,
                        "text": response['text']
                    }
                )
    
    return {"status": "success"}