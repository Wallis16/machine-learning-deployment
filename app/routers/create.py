from fastapi import APIRouter, HTTPException, Depends
from models.user_registry import UserRegistry
from databases.mongodb import get_database

router = APIRouter()

@router.post("/data/", tags=['CRUD'])
async def create_data(registry: UserRegistry, collection = Depends(get_database)):
    try:
        result = await collection.insert_one(registry.dict())
        inserted_data = await collection.find_one({"_id": result.inserted_id})
        inserted_data["_id"] = str(inserted_data["_id"])

        return inserted_data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))