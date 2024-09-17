from fastapi import FastAPI
from decouple import config
from src.models.models import Chat

app = FastAPI()

FRONT_END_URL = config('FRONT_END_URL')
print(FRONT_END_URL)


@app.post('/ia/')
async def welcome(userMessage : str):
    chat = Chat(userMessage=userMessage)
    chat.iaResponse = "hola que tal" 
    return chat.model_dump()
