from fastapi import APIRouter

from ....domain.repository import ManaCostTypeRepository
from ....domain.schemas import ManaCostTypeSchema, ManaCostTypeCreateSchema
from ....domain.services import ManaCostTypeService

router = APIRouter(
    prefix="/v1/ManaCostTypes",
    tags=["ManaCostType"]
)


@router.get("")
async def get_mana_cost_types() -> list[ManaCostTypeSchema]:
    mana_cost_types = await ManaCostTypeService(ManaCostTypeRepository).get_types()
    return mana_cost_types


@router.put("")
async def create_mana_cost_type(
        user: ManaCostTypeCreateSchema,
) -> dict[str, object | int]:
    mana_cost_type = await ManaCostTypeService(ManaCostTypeRepository).save_mana_cost_type(user)
    return {"mana_cost_type": mana_cost_type}
