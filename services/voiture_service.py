from models.voiture import Voiture
from typing import List, Optional

# CREATE a new car
async def create_voiture(data: dict) -> Voiture:
    voiture = Voiture(**data)
    await voiture.insert()
    return voiture

# GET all cars
async def get_voitures() -> List[Voiture]:
    return await Voiture.find_all().to_list()

# GET one car by ID
async def get_voiture(voiture_id: str) -> Optional[Voiture]:
    return await Voiture.get(voiture_id)

# UPDATE a car
async def update_voiture(voiture_id: str, data: dict) -> Optional[Voiture]:
    voiture = await Voiture.get(voiture_id)
    if not voiture:
        return None
    for key, value in data.items():
        setattr(voiture, key, value)
    await voiture.save()
    return voiture

# DELETE a car
async def delete_voiture(voiture_id: str) -> bool:
    voiture = await Voiture.get(voiture_id)
    if not voiture:
        return False
    await voiture.delete()
    return True