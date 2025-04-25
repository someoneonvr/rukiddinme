# utils/message_schema.py

from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from datetime import datetime
import uuid


class Message(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    thread_id: str
    sender: str
    recipient: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    priority: Literal["low", "normal", "high"] = "normal"
    subject: Optional[str] = None
    content: str
    context: Optional[dict] = None
    message_type: Literal["request", "response", "update", "feedback"] = "request"
    requires_ack: bool = False


class MessageThread(BaseModel):
    thread_id: str
    participants: List[str]
    messages: List[Message] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def add_message(self, message: Message):
        self.messages.append(message)
        self.updated_at = datetime.utcnow()
