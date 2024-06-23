# Use an official Python runtime as a parent image
FROM python:3.11.6-slim

ARG MONGODB_USER
ARG MONGODB_PASSWORD
ARG MONGODB_DATABASE
ARG MLFLOW_URI
ARG MLFLOW_EXPERIMENT 

ENV user=$MONGODB_USER
ENV password=$MONGODB_PASSWORD
ENV database=$MONGODB_DATABASE
ENV mlflow_uri=$MLFLOW_URI
ENV mlflow_experiment=$MLFLOW_EXPERIMENT

WORKDIR /app_backend

# Copy the current directory contents into the container at /app
COPY . /app_backend

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the MLflow UI port
EXPOSE 8000

# Run MLflow server when the container launches
CMD ["python", "app/main.py"]
