from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    telegram_id: str
    username: Optional[str] = None


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True


class SubscriptionBase(BaseModel):
    plan: str


class SubscriptionCreate(SubscriptionBase):
    user_id: int


class SubscriptionResponse(BaseModel):
    id: int
    user_id: int
    plan: str
    status: str
    start_date: datetime
    end_date: datetime

    class Config:
        from_attributes = True
