from fastapi import FastAPI
from app.views.addition import router as addition_router
import logging
from app.utils.logging import setup_logging

setup_logging()
app = FastAPI()

app.include_router(addition_router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
