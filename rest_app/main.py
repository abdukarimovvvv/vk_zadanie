from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import uvicorn
import os
import importlib
from .database import get_db  # Использование относительного импорта

app = FastAPI()

routes_dir = os.path.join(os.path.dirname(__file__), 'routes')
for filename in os.listdir(routes_dir):
    if filename.endswith('_controller.py'):
        module_name = filename[:-3]
        module = importlib.import_module(f'rest_app.routes.{module_name}')
        if hasattr(module, 'router'):
            app.include_router(module.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the JSON document processing app"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
