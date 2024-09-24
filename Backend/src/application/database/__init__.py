from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from ...config import config

engine = create_async_engine(config["DATABASE_ENGINE"])
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, autoflush=False)

# sync_engine = create_engine(config["DATABASE_ENGINE"])
# session_maker = sessionmaker(sync_engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_async_session():
    async with async_session_maker() as session:
        yield session


def create_filters(model, **filters_by):
    filters = []
    for field, condition in filters_by.items():
        if isinstance(condition, dict):
            for op, value in condition.items():
                if op == 'eq':
                    filters.append(getattr(model, field) == value)
                elif op == 'gt':
                    filters.append(getattr(model, field) > value)
                elif op == 'lt':
                    filters.append(getattr(model, field) < value)
        else:
            filters.append(getattr(model, field) == condition)
    return filters


__all__ = [
    "Base",
    "get_async_session",
    "models",
    "create_filters",
    "async_session_maker",
    "session_maker",
]
