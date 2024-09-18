from pydantic import BaseModel, Field
from typing import Optional, Union
from fastapi import UploadFile


class ChatResponse(BaseModel):
    userMessage: str
    iaResponse: Optional[str] = None
    files: Optional[list[str]] = None


class UserMesssage(BaseModel):
    userMessage: str
    uploadFiles: Optional[UploadFile] = None
