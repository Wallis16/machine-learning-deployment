from pydantic import BaseModel

class Parameters(BaseModel):
    passenger_count: list
    trip_distance: list
    payment_type: list

class InferenceData(BaseModel):
    run_id: str
    mlflow_uri: str
    inference_data: Parameters
