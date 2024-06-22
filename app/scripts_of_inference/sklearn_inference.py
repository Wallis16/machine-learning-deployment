import mlflow
import pandas as pd

def inference(data):

    #logged_model = "mlflow/data/mlartifacts/1/a21aa525639d4b069c48c8cd052cd866/artifacts/model"
    ready_data = data.dict()
    logged_model = ready_data["logged_model"]
    loaded_model = mlflow.pyfunc.load_model(logged_model)

    #data = {"passenger_count": [3], "trip_distance": [16], "payment_type": [2]}

    data_ = pd.DataFrame.from_dict(ready_data["inference_data"])

    return loaded_model.predict(pd.DataFrame(data_))[0]
