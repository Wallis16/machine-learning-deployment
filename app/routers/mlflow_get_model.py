from fastapi import APIRouter, HTTPException
from mlflow import MlflowClient

import mlflow

router = APIRouter()

@router.get("/get_run_id/", tags=['ML registry'])
async def get_run_id(mlflow_server: str, experiment_name: str,
                        metric: str, sort_by: str):

    try:

        mlflow.set_tracking_uri(mlflow_server) 
        runs = mlflow.search_runs(experiment_names=[experiment_name], order_by=[f"metrics.{metric} {sort_by}"])  

        return runs["run_id"][0]

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))