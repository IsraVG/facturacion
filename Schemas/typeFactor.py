from pydantic import BaseModel
from typing import Optional

class TypeFactor( BaseModel ):
    id: Optional[int]
    description: str
    status: Optional[int] = 1