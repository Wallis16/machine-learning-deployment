"""<>"""
from urllib.parse import urlparse
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from pandas import DataFrame
from optuna import Trial
# from dotenv import load_dotenv, find_dotenv

import numpy as np
import mlflow

# load_dotenv(find_dotenv())

def objective(trial : Trial, x : DataFrame, y : np.ndarray,
               collection_name: str, mlflow_uri: str) -> float:
    """<>"""

    mlflow.set_tracking_uri(mlflow_uri)
    mlflow.set_experiment(collection_name)

    with mlflow.start_run():
        n_estimators = trial.suggest_int('n_estimators', 2, 20)
        max_depth = int(trial.suggest_float('max_depth', 1, 32, log=True))

        clf = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth)

        mean_score = cross_val_score(clf, x, y, n_jobs=-1, cv=3).mean()

        clf.fit(x, y)

        mlflow.log_params(trial.params)
        mlflow.log_metric('mean_score', mean_score)
        mlflow.sklearn.log_model(clf, 'random_forest_model')
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        if tracking_url_type_store != 'file':
            mlflow.sklearn.log_model(clf, 'model', registered_model_name='RFR_')
        else:
            mlflow.sklearn.log_model(clf, 'model')
    return mean_score
