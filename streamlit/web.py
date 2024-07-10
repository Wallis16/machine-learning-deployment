import streamlit as st
import json
import requests

import os

url_streamlit = os.getenv('URL_STREAMLIT')

st.title("ML platform")

option = st.selectbox("Select the ML module",("training","inference"))

if option == "training":

    st.write("")
    st.write("Fill the fields")

    dataset_name = st.text_input("Dataset name", "tlc_trip_data_1")

    if st.button('Run Training'):
        res = requests.get(f'{url_streamlit}/run_training/?collection_name={dataset_name}')
        dict_result = res.json()
        st.subheader(f'Best model related to this training - Accuracy: {dict_result["accuracy"]}, Trial: {dict_result["trial"]}, Number of estimators: {dict_result["n_estimators"]}, Max depths: {dict_result["max_depth"]}')

if option == "inference":

    st.write("")
    st.write("Fill the fields")

    mlflow_server = st.text_input("mlflow server", "http://localhost:5000/")
    experiment_name = st.text_input("experiment name", "tlc_trip_data_2")
    metric = st.text_input("metric", "mean_score")
    sort = st.text_input("sort", "DESC")

    if st.button('Get run id'):
        run_id = requests.get(f'{url_streamlit}/get_run_id/?mlflow_server={mlflow_server}&experiment_name={experiment_name}&metric={metric}&sort_by={sort}')
        st.write(run_id.json())

    logged_model = st.text_input("Logged model", "")

    st.write("Inference data")

    passenger_count = st.text_input("passenger_count", "1,2,3,4")
    experiment_name = st.text_input("experiment_name", "1")
    trip_distance = st.text_input("trip_distance", "miles")
    payment_type = st.text_input("payment_type", "0, 1, 2")

    input = {
    "logged_model": f"mlflow/data/mlartifacts/{experiment_name}/{logged_model}/artifacts/model",
    "inference_data": {
        "passenger_count": [
        passenger_count
        ],
        "trip_distance": [
        trip_distance
        ],
        "payment_type": [
        payment_type
        ]
    }
    }

    if st.button('Run Inference'):
        res = requests.post(url=f'{url_streamlit}/inference/', data=json.dumps(input))
        st.subheader(f'Fare estimative - {res.json()}')