from fastapi import APIRouter, HTTPException
from app.models.request_response import AdditionRequest, AdditionResponse
from app.controller.addition_controller import perform_addition

router = APIRouter()

@router.post("/add", response_model=AdditionResponse)
async def add_numbers(request: AdditionRequest):
    result = perform_addition(request.batchcid, request.payload)
    if result["status"] == "error":
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return result
