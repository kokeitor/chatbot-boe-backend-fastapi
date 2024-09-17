from fastapi import FastAPI
from decouple import config
from src.models.models import ChatResponse, UserMesssage
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

FRONT_END_URL = config('FRONT_END_URL')
print(f"FRONT_END_URL : {FRONT_END_URL}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def welcome():
    return {"response": "hola welcome!"}

@app.get('/getiaresponse/{userMessage}')
async def welcome(userMessage : str,):
    chat = ChatResponse(userMessage=userMessage)
    chat.iaResponse = "hola que tal" 
    return chat.model_dump()


@app.post('/iaresponse/')
async def getIaResponse(userMessage : UserMesssage):
    chat = ChatResponse(userMessage=userMessage.userMessage, files=userMessage.files)
    chat.iaResponse = "hola que tal" 
    return chat.model_dump()


