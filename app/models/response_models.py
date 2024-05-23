from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class AdditionResponse(BaseModel):
    batchid: str = Field(..., example="id0101")
    response: List[int] = Field(..., example=[3, 7])
    status: str = Field(..., example="complete")
    started_at: datetime
    completed_at: datetime
