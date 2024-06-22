from fastapi import APIRouter, HTTPException
from scripts_of_inference.sklearn_inference import inference
from models.inference_data import InferenceData
router = APIRouter()

@router.post("/inference/", tags=['ML inference'])
async def run_inference(inference_data: InferenceData):
    try:

        return inference(inference_data)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))