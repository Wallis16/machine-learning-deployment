"""<>"""
from fastapi import APIRouter, HTTPException
from mlflow import MlflowClient

import mlflow

router = APIRouter()

@router.get('/run_tags/', tags=['ML registry'])
async def run_tags(mlflow_server: str, registry_model_name: str,
                        tag_key: str, tag_value: str):
    """<>"""
    try:

        mlflow.set_tracking_uri(mlflow_server)
        client = MlflowClient(mlflow.get_tracking_uri())
        client.set_registered_model_tag(registry_model_name, tag_key, tag_value)

        return 'model registration executed'

    except Exception as e:
        raise HTTPException(status_code=400) from e
