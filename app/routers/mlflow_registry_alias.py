from fastapi import APIRouter, HTTPException
from mlflow import MlflowClient

import mlflow

router = APIRouter()

@router.get("/run_alias/", tags=['ML registry'])
async def run_alias(mlflow_server: str, registry_model_name: str,
                        tag_name: str, version_name: str):

    try:

        mlflow.set_tracking_uri(mlflow_server)
        client = MlflowClient(mlflow.get_tracking_uri()) 
        client.set_registered_model_alias(registry_model_name,
                                           tag_name, version_name) 

        return "model registration executed"

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))