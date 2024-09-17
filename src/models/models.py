from pydantic import BaseModel, Field
from typing import Optional


class ChatResponse(BaseModel):
    userMessage: str
    iaResponse: Optional[str] = None
    files : Optional[list[str]] = None

class UserMesssage(BaseModel):
    userMessage: str
    files : Optional[list[str]] = None

