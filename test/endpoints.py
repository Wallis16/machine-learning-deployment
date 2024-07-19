"""<>"""
import json
import requests

def test_get_id():
    """<>"""
    server = 'http://host.docker.internal:5000'
    experiment_name = 'tlc_trip_data_1'
    metric = 'mean_score'
    sort_by = 'DESC'
    url = 'http://localhost:8000/get_run_id/'
    res = requests.get(f'{url}?mlflow_server={server}&' +
        f'experiment_name={experiment_name}&metric={metric}&sort_by={sort_by}',
        timeout=1.5)
    assert res.status_code == 200

def test_inference():
    """<>"""
    server = 'http://host.docker.internal:5000'
    experiment_name = 'tlc_trip_data_1'
    metric = 'mean_score'
    sort_by = 'DESC'

    run_id = requests.get('http://localhost:8000/get_run_id/?' +
        f'mlflow_server={server}&experiment_name={experiment_name}&' +
        f'metric={metric}&sort_by={sort_by}', timeout=1.5)

    res = requests.post(url = 'http://localhost:8000/inference/', data=json.dumps({
    'logged_model': f'mlflow/data/mlartifacts/1/{run_id.text[1:-1]}/artifacts/model',
    'inference_data': {
    'passenger_count': [2],
    'trip_distance': [23],
    'payment_type': [1]
    }
    }), timeout=1.5)
    assert res.status_code == 200
