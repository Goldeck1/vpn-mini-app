from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User, Subscription
from app.schemas.user import UserCreate, SubscriptionCreate
from datetime import datetime, timedelta


class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_or_create_user(self, user_data: UserCreate) -> User:
        result = await self.db.execute(
            select(User).where(User.telegram_id == user_data.telegram_id)
        )
        user = result.scalar_one_or_none()

        if not user:
            user = User(**user_data.model_dump())
            self.db.add(user)
            await self.db.commit()
            await self.db.refresh(user)

        return user

    async def get_user_by_telegram_id(self, telegram_id: str) -> User | None:
        result = await self.db.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        return result.scalar_one_or_none()


class SubscriptionService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_subscription(self, user_id: int, plan: str) -> Subscription:
        plan_days = {
            "1_month": 30,
            "3_month": 90,
            "12_month": 365,
        }

        end_date = datetime.utcnow() + timedelta(days=plan_days.get(plan, 30))

        subscription = Subscription(
            user_id=user_id,
            plan=plan,
            end_date=end_date,
        )

        self.db.add(subscription)
        await self.db.commit()
        await self.db.refresh(subscription)

        return subscription

    async def get_user_subscriptions(self, user_id: int) -> list[Subscription]:
        result = await self.db.execute(
            select(Subscription).where(Subscription.user_id == user_id)
        )
        return result.scalars().all()
