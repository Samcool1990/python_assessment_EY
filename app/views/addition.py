from fastapi import APIRouter, HTTPException
from app.models.request_models import AdditionRequest
from app.models.response_models import AdditionResponse
from app.controller.addition_controller import addition_worker
from datetime import datetime
import multiprocessing

router = APIRouter()

@router.post("/add", response_model=AdditionResponse)
async def add_numbers(request: AdditionRequest):
    started_at = datetime.utcnow()
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    process = multiprocessing.Process(target=addition_worker, args=(request.payload, return_dict))
    process.start()
    process.join()

    if 'error' in return_dict:
        raise HTTPException(status_code=500, detail=return_dict['error'])

    completed_at = datetime.utcnow()
    response = AdditionResponse(
        bathcid=request.bathcid,
        response=return_dict['result'],
        status="complete",
        started_at=started_at,
        completed_at=completed_at
    )
    return response
