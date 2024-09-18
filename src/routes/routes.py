from fastapi import HTTPException, APIRouter
from src.models.models import ChatResponse, UserMesssage
import os

UPLOAD_DIR = os.path.join(os.getcwd(), 'src', 'assets', 'uploads')
print(f"UPLOAD_DIR : {UPLOAD_DIR}")

iaResponse = APIRouter()


@iaResponse.post('/iaresponse/{userMessage}')
async def welcome(userMessage: str,):
    chat = ChatResponse(userMessage=userMessage)
    chat.iaResponse = "hola que tal jajajajajaa"
    return chat.model_dump()


@iaResponse.post('/iaresponse/')
async def getIaResponse(userMessage: UserMesssage):
    print(userMessage)
    print(userMessage.model_dump())
    if userMessage.uploadFiles:
        fileNames = []
        for file in userMessage.uploadFiles:
            print(f"file : {file}")
            fileName = file.filename
            fileNames.append(fileName)
            fileContent = await file.read()
            with open(UPLOAD_DIR + f"/{fileName}", "wb") as f:
                f.write(fileContent)
        chat = ChatResponse(
            userMessage=userMessage.userMessage, files=fileNames)
    else:
        chat = ChatResponse(userMessage=userMessage.userMessage, files=[""])
    chat.iaResponse = "hola que tal jajajajajaa"
    return chat.model_dump()
