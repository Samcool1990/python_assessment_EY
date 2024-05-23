from fastapi import FastAPI
from app.views import addition

app = FastAPI()

app.include_router(addition.router, prefix="/api/v1", tags=["addition"])

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application"}
