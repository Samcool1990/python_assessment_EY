from pydantic import BaseModel, Field, StrictInt
from typing import List

class AdditionRequest(BaseModel):
    batchid: str = Field(..., example="id0101")
    payload: List[List[StrictInt]] = Field(..., example=[[1, 2], [3, 4]])
