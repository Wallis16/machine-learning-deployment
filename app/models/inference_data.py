from pydantic import BaseModel

class Parameters(BaseModel):
    passenger_count: list
    trip_distance: list
    payment_type: list

class InferenceData(BaseModel):
    logged_model: str
    inference_data: Parameters