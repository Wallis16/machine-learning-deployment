"""<>"""

from scripts_of_training.optuna_objective import objective
from sklearn.model_selection import train_test_split

import optuna

numerical_features = ['passenger_count', 'trip_distance',
                           'payment_type', 'fare_amount']

def skelarn_model(data_for_training, collection_name):
    """<>"""

    data_for_training = data_for_training[numerical_features]

    all_data = data_for_training.dropna()

    x, y = all_data[['passenger_count', 'trip_distance',
                      'payment_type']], all_data[['fare_amount']]

    x_train, _, y_train, _ = train_test_split(x, y.values.ravel(),
                                    test_size=0.33, random_state=42)
    study = optuna.create_study(study_name='optimization', direction='maximize')
    study.optimize(lambda trial: objective(trial, x_train, y_train, collection_name), n_trials=2)

    best_trial = study.best_trial

    return ({"accuracy": best_trial.value,
     "trial": best_trial.number,
    "n_estimators": best_trial.params["n_estimators"],
    "max_depth": best_trial.params["max_depth"]})
