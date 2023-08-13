from pydantic import BaseModel
from typing import Optional

class UnitKey( BaseModel ):
    id: Optional[int]
    code: str
    description: str
    note: str
    status: Optional[int] = 1