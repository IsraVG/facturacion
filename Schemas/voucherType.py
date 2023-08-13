from turtle import st
from pydantic import BaseModel
from typing import Optional

class VoucherType( BaseModel ):
    id: Optional[int]
    code: str
    description: str
    status: Optional[int] = 1