from pydantic import BaseModel
from typing import Optional

class Taxation( BaseModel ):
    id: Optional[int]
    code: str
    description: str
    status: Optional[int] = 1