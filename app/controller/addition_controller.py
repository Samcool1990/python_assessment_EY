from fastapi import APIRouter, HTTPException
from datetime import datetime
from app.models.request_models import AdditionRequest
from app.models.response_models import AdditionResponse
from app.views.addition import perform_addition

router = APIRouter()

@router.post("/add", response_model=AdditionResponse)
async def add_numbers(request: AdditionRequest):
    started_at = datetime.utcnow()
    try:
        result = perform_addition(request.payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    completed_at = datetime.utcnow()
    response = AdditionResponse(
        batchid=request.batchid,
        response=result,
        status="complete",
        started_at=started_at,
        completed_at=completed_at
    )
    return response
