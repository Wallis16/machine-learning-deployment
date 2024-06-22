from fastapi import APIRouter, HTTPException, Depends
from bson import ObjectId
from databases.mongodb import get_database

router = APIRouter()

@router.delete("/delete_data/", tags=['CRUD'])
async def delete_data(_id: str, collection = Depends(get_database)):
    try:
        # Check if the provided ID exists in the database
        if await collection.count_documents({"_id": ObjectId(_id)}) == 0:
            raise HTTPException(status_code=404, detail="Data not found")
        
        await collection.delete_one({"_id": ObjectId(_id)})
        
        # Return a success message
        return {"message": "Data removed successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))