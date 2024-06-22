from fastapi import Depends, FastAPI
from auth.dependencies import get_query_token, get_token_header
from routers import training, inference, mlflow_registry_alias, mlflow_registry_tags, mlflow_get_model
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

origins = [
    'http://localhost.tiangolo.com',
    'https://localhost.tiangolo.com',
    'http://localhost',
    'http://localhost:8080',
]

app = FastAPI(title='web_service_ML')

app.include_router(training.router)
app.include_router(inference.router)
app.include_router(mlflow_registry_alias.router)
app.include_router(mlflow_registry_tags.router)
app.include_router(mlflow_get_model.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
