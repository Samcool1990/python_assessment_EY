from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class AdditionRequest(BaseModel):
    batchcid: str = Field(..., example="id0101")
    payload: List[List[int]] = Field(..., example=[[1, 2], [3, 4]])

class AdditionResponse(BaseModel):
    batchcid: str
    response: List[int]
    status: str
    started_at: datetime
    completed_at: datetime
