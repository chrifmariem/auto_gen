from fastapi import APIRouter, HTTPException
from services.voiture_service import (
    create_voiture, get_voitures,
    get_voiture, update_voiture, delete_voiture
)

router = APIRouter(prefix="/voitures", tags=["Voitures"])

@router.post("/")
async def create(data: dict):
    return await create_voiture(data)

@router.get("/")
async def read_all():
    return await get_voitures()

@router.get("/{voiture_id}")
async def read_one(voiture_id: str):
    voiture = await get_voiture(voiture_id)
    if not voiture:
        raise HTTPException(status_code=404, detail="Voiture not found")
    return voiture

@router.put("/{voiture_id}")
async def update(voiture_id: str, data: dict):
    voiture = await update_voiture(voiture_id, data)
    if not voiture:
        raise HTTPException(status_code=404, detail="Voiture not found")
    return voiture

@router.delete("/{voiture_id}")
async def delete(voiture_id: str):
    success = await delete_voiture(voiture_id)
    if not success:
        raise HTTPException(status_code=404, detail="Voiture not found")
    return {"message": "Voiture deleted successfully"}