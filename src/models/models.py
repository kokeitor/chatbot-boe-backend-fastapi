from pydantic import BaseModel, Field
from typing import Optional


class Chat(BaseModel):
    userMessage: str
    iaResponse: Optional[str] = None
    files : Optional[list[str]] = None
