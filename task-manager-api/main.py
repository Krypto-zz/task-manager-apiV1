from fastapi import FastAPI
from routes.task_routes import router

app_task = FastAPI()

app_task.include_router(router)