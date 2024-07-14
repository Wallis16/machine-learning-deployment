# Use an official Python runtime as a parent image
FROM python:3.11.6-slim

WORKDIR /streamlit

# Copy the current directory contents into the container at /app
COPY . /streamlit

# Install any needed dependencies specified in requirements.txt
RUN pip install streamlit==1.31.1

# Expose the MLflow UI port
EXPOSE 8501

RUN python setup.py sdist bdist_wheel

RUN pip install dist/mycommand-1.0.5-py3-none-any.whl

CMD ["mycommand"]