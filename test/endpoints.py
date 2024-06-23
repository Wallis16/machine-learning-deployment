#mlflow

import requests
import json
def test_training():
    dataset = 'tlc_trip_data_1'
    requests.get(f'http://localhost:8000/run_training/?collection_name={dataset}')
    assert True

def test_get_id():
    server = "http://localhost:5000/"
    experiment_name = "tlc_trip_data_1"
    metric = "mean_score"
    sort_by = "DESC"
    requests.get(f'http://localhost:8000/get_run_id/?mlflow_server={server}&experiment_name={experiment_name}&metric={metric}&sort_by={sort_by}')
    assert True

def test_inference():
    server = "http://localhost:5000/"
    experiment_name = "tlc_trip_data_1"
    metric = "mean_score"
    sort_by = "DESC"
    
    run_id = requests.get(f'http://localhost:8000/get_run_id/?mlflow_server={server}&experiment_name={experiment_name}&metric={metric}&sort_by={sort_by}')
    
    requests.post(url = 'http://localhost:8000/inference/', data=json.dumps({
    "logged_model": f"mlflow/data/mlartifacts/1/{run_id}/artifacts/model",
    "inference_data": {
    "passenger_count": [2],
    "trip_distance": [23],
    "payment_type": [1]
    }
    }))
    assert True