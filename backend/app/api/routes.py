from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.user_service import UserService, SubscriptionService
from app.schemas.user import UserCreate, UserResponse, SubscriptionCreate, SubscriptionResponse

router = APIRouter(prefix="/api", tags=["users"])


@router.post("/users", response_model=UserResponse)
async def create_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    service = UserService(db)
    return await service.get_or_create_user(user_data)


@router.get("/users/{telegram_id}", response_model=UserResponse)
async def get_user(telegram_id: str, db: AsyncSession = Depends(get_db)):
    service = UserService(db)
    user = await service.get_user_by_telegram_id(telegram_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.post("/subscriptions", response_model=SubscriptionResponse)
async def create_subscription(
    subscription_data: SubscriptionCreate, db: AsyncSession = Depends(get_db)
):
    service = SubscriptionService(db)
    return await service.create_subscription(
        user_id=subscription_data.user_id, plan=subscription_data.plan
)


@router.get("/users/{user_id}/subscriptions", response_model=list[SubscriptionResponse])
async def get_user_subscriptions(user_id: int, db: AsyncSession = Depends(get_db)):
    service = SubscriptionService(db)
    return await service.get_user_subscriptions(user_id)
