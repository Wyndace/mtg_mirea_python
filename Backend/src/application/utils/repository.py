from abc import ABC, abstractmethod
from sqlalchemy import insert, select, delete, and_

from ..database import async_session_maker, create_filters


class AbstractRepositoryDatabase(ABC):
    @abstractmethod
    async def add_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def remove(self, *args, **kwargs):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepositoryDatabase):
    model = None

    async def add_one(self, data: dict = None) -> object:
        if data is None:
            data = {}

        async with async_session_maker() as db_session:
            stmt = insert(self.model).values(**data).returning(self.model)
            result = await db_session.execute(stmt)
            await db_session.commit()
            return result.scalar_one().to_read_model()

    async def find_one(self, **filter_by) -> object:
        async with async_session_maker() as db_session:
            stmt = select(self.model).filter_by(**filter_by)
            result = await db_session.execute(stmt)
            return result.scalar_one().to_read_model()

    async def remove(self, **filters_by):
        async with async_session_maker() as db_session:
            filters = create_filters(self.model, **filters_by)
            stmt = delete(self.model).filter(and_(*filters))
            await db_session.execute(stmt)
            await db_session.commit()

    async def find_all(self, **filters_by) -> list[object]:
        async with async_session_maker() as db_session:
            filters = create_filters(self.model, **filters_by)
            stmt = select(self.model).filter(and_(*filters))
            result = await db_session.execute(stmt)
            result_list = [row[0].to_read_model() for row in result.all()]
            return result_list
