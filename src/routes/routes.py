from fastapi import HTTPException, APIRouter
from src.models.models import ChatResponse
from typing import Optional
from fastapi import UploadFile, File, Form
import os

UPLOAD_DIR = os.path.join(os.getcwd(), 'src', 'assets', 'uploads')
print(f"UPLOAD_DIR : {UPLOAD_DIR}")

iaResponse = APIRouter()


@iaResponse.post('/iaresponse/{userMessage}')
async def welcome(userMessage: str,):
    chat = ChatResponse(userMessage=userMessage)
    chat.iaResponse = "hola que tal jajajajajaa"
    return chat.model_dump()


@iaResponse.post("/iaresponse/")
async def getIaResponse(
    userMessage: str = Form(...),
    uploadFiles: Optional[list[UploadFile]] = File(None)
):
    print(f"uploadFiles : {uploadFiles}")
    if uploadFiles:
        fileNames = []
        for file in uploadFiles:
            fileName = file.filename
            fileNames.append(fileName)
            fileContent = await file.read()
            with open(os.path.join(UPLOAD_DIR, fileName), "wb") as f:
                f.write(fileContent)
        chat = ChatResponse(
            userMessage=userMessage,
            iaResponse="hola que tal jajajajajaa",
            files=fileNames
        )
    else:
        chat = ChatResponse(
            userMessage=userMessage,
            iaResponse="hola que tal jajajajajaa",
            files=[]
        )
    return chat
