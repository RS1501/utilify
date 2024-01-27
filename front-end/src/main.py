from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class UserMessage(BaseModel):
    text: str

@app.post("/api/sendMessage")
async def send_message(user_message: UserMessage):
    user_input = user_message.text

    # Split the user's input into a list of responses
    user_responses = [response.strip() for response in user_input.split(',')]

    # Extract responses to individual questions
    monthly_spend, international_minutes, benefits = user_responses[:3]

    return {"botResponse": monthly_spend}