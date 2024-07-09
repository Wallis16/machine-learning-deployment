import mlflow
import pandas as pd
import os 

from mlflow import MlflowClient

def inference(data):

    ready_data = data.dict()
    run_id = ready_data["run_id"]

    mlflow.set_tracking_uri(ready_data["mlflow_uri"])
    client = MlflowClient(mlflow.get_tracking_uri())
    
    try:
        os.makedirs(f"{os.getcwd()}/inference_models/{run_id}/")
    except Exception as e:
        print(e)
        pass

    client.download_artifacts(ready_data["run_id"], "model", f"{os.getcwd()}/inference_models/{run_id}/")
    loaded_model = mlflow.pyfunc.load_model(f"{os.getcwd()}/inference_models/{run_id}/model")

    data_ = pd.DataFrame.from_dict(ready_data["inference_data"])

    return loaded_model.predict(pd.DataFrame(data_))[0]
