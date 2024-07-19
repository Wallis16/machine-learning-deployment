"""<>"""
import os
import json
import requests
import streamlit as st

url_backend = os.getenv('URL_BACKEND')

st.title('ML platform')

option = st.selectbox('Select the ML module',('training','inference'))

if option == 'training':

    st.write('')
    st.write('Fill the fields')

    dataset_name = st.text_input('Dataset name', 'tlc_trip_data_1')
    mlflow_server = st.text_input('mlflow uri', 'http://localhost:5000/')

    if st.button('Run Training'):
        res = requests.get(f'{url_backend}/run_training/?' +
                        f'collection_name={dataset_name}&mlflow_uri={mlflow_server}',
                        timeout=120)
        dict_result = res.json()
        st.subheader('Best model related to this training -' +
        f'Accuracy: {dict_result["accuracy"]}, Trial: {dict_result["trial"]},' +
        f'Number of estimators: {dict_result["n_estimators"]},' +
        f'Max depths: {dict_result["max_depth"]}')

if option == 'inference':

    st.write('')
    st.write('Fill the fields')

    mlflow_server = st.text_input('mlflow server', 'http://localhost:5000/')
    experiment_name = st.text_input('experiment name', 'tlc_trip_data_2')
    metric = st.text_input('metric', 'mean_score')
    sort = st.text_input('sort', 'DESC')

    if st.button('Get run id'):
        run_id = requests.get(f'{url_backend}/get_run_id/?' +
            f'mlflow_server={mlflow_server}' +
            f'&experiment_name={experiment_name}&metric={metric}&sort_by={sort}',
            timeout = 3)
        st.write(run_id.json())

    st.write('Inference data')

    passenger_count = st.text_input('passenger_count', '1,2,3,4')
    trip_distance = st.text_input('trip_distance', 'miles')
    payment_type = st.text_input('payment_type', '0, 1, 2')
    run_id_inference =  st.text_input('run id', '')
    mlflow_server = st.text_input('mlflow uri', 'http://localhost:5000/')

    input_inference = {
        'run_id': run_id_inference,
        'mlflow_uri': mlflow_server,
        'inference_data': {
            'passenger_count': [
            passenger_count
            ],
            'trip_distance': [
            trip_distance
            ],
            'payment_type': [
            payment_type
            ]
            }
            }

    if st.button('Run Inference'):
        res = requests.post(url=f'{url_backend}/inference/',
                             data=json.dumps(input_inference),
                            timeout=3)
        st.subheader(f'Fare estimative - {res.json()}')
