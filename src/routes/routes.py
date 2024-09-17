from fastapi import HTTPException, APIRouter
from src.models.models import ChatResponse, UserMesssage

iaResponse = APIRouter()

@iaResponse.get('/iaresponse/{userMessage}')
async def welcome(userMessage : str,):
    chat = ChatResponse(userMessage=userMessage)
    chat.iaResponse = "hola que tal jajajajajaa" 
    return chat.model_dump()


@iaResponse.post('/iaresponse/')
async def getIaResponse(userMessage : UserMesssage):
    chat = ChatResponse(userMessage=userMessage.userMessage, files=userMessage.files)
    chat.iaResponse = "hola que tal jajajajajaa" 
    return chat.model_dump()
