from fastapi import APIRouter, HTTPException, Depends
from scripts_of_training import optuna_run
from databases.mongodb import get_database

import pandas as pd

router = APIRouter()

@router.get("/run_training/", tags=['ML training'])
async def run_training(collection_name: str, collection_ = Depends(get_database)):

    try:

        collection = collection_[collection_name]
        documents = collection.find()
        data_for_training = pd.DataFrame(documents)
        return optuna_run.skelarn_model(data_for_training, collection_name)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))